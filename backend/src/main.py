from flask import Flask, jsonify, request
from flask_cors import CORS
from flask_swagger_ui import get_swaggerui_blueprint
from flask_sqlalchemy import SQLAlchemy
import redis
import requests
import decimal
import csv
import json
import os
import io
from bs4 import BeautifulSoup
from .models import db, Producao  # Novo
from database import save_to_database, get_from_database  # Novo
import logging
logging.basicConfig(
    level=logging.DEBUG,
    format='%(asctime)s - %(levelname)s - %(message)s',
    handlers=[
        logging.FileHandler('debug.log'),
        logging.StreamHandler()
    ]
)

app = Flask(__name__, static_folder='../static', static_url_path='/static')

CORS(app)  # Libera CORS para todas as rotas e origens

BACKUP_DIR = 'backup'

# Configuração do Banco de Dados
app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://user:password@embrapa-db:5432/vitivinicultura'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db.init_app(app)  # Garanta que esta linha está presente

REDIS_HOST = os.getenv("REDIS_HOST", "localhost")
REDIS_PORT = 6379

# Inicialização das extensões
redis_client = redis.Redis(
    host=os.getenv("REDIS_HOST", "localhost"),
    port=int(os.getenv("REDIS_PORT", "6379")),
    db=0,
    decode_responses=True
)

# Configuração do Swagger   
SWAGGER_URL = '/api/docs'
API_URL = '/static/swagger.json'
swaggerui_blueprint = get_swaggerui_blueprint(
    SWAGGER_URL,
    API_URL,
    config={'app_name': "API Vitivinicultura Embrapa"}
)
app.register_blueprint(swaggerui_blueprint, url_prefix=SWAGGER_URL)

@app.route('/')
def index():
    return jsonify({"message": "Bem-vindo à API Vitivinicultura Embrapa! Acesse /api/docs para a documentação."}) 

def parse_quantity(value):
    """Converte valores numéricos com formatação para inteiros"""
    try:
        return int(value.replace('.', '')) if value not in ('-', '') else None
    except:
        return None

def scrape_production(year):
    """Realiza web scraping dos dados diretamente do site"""
    url = f'http://vitibrasil.cnpuv.embrapa.br/index.php?opcao=opt_02&ano={year}'
    response = requests.get(url)
    response.raise_for_status()
    
    soup = BeautifulSoup(response.text, 'html.parser')
    table = soup.find('table', {'class': 'tb_dados'}) or soup.find('table')
    
    if not table:
        return None

    data = []
    current_category = None
    
    for row in table.find('tbody').find_all('tr'):
        cells = row.find_all('td')
        if not cells:
            continue
            
        cell_classes = cells[0].get('class', [])
        
        if 'tb_item' in cell_classes:
            current_category = {
                'produto': cells[0].text.strip(),
                'quantidade': parse_quantity(cells[1].text.strip()),
                'subprodutos': []
            }
            data.append(current_category)
        elif 'tb_subitem' in cell_classes and current_category:
            subproduct = {
                'produto': cells[0].text.strip(),
                'quantidade': parse_quantity(cells[1].text.strip())
            }
            current_category['subprodutos'].append(subproduct)

    # Extrair total
    total = None
    tfoot = table.find('tfoot', {'class': 'tb_total'})
    if tfoot:
        cells = tfoot.find_all('td')
        if len(cells) >= 2:
            total = parse_quantity(cells[1].text.strip())

    return {
        'ano': year,
        'dados': data,
        'total': total
    }

def load_backup(year):
    """Carrega dados de arquivos CSV locais no formato da Embrapa"""
    year_str = str(year)
    csv_path = os.path.join(BACKUP_DIR, f'Producao_{year}.csv')
    
    if not os.path.exists(csv_path):
        return None

    try:
        with open(csv_path, 'r', encoding='utf-8') as f:
            reader = csv.DictReader(f, delimiter=';')
            
            data = []
            current_category = None
            fieldnames = reader.fieldnames
                
            # Verifica se o ano existe no CSV
            if year_str not in fieldnames:
                return None
                
            for row in reader:
                # Pula linhas de cabeçalho adicional
                if row['id'] == 'id':
                    continue
                
                # Determina hierarquia pelo ID
                produto_id = int(row['id'])
                
                # Categorias principais (IDs específicos)
                if produto_id in [1,5,9,15,24,37,46]:
                    current_category = {
                        'produto': row['produto'].strip(),
                        'quantidade': parse_quantity(row[year_str]),
                        'subprodutos': []
                    }
                    data.append(current_category)
                # Subprodutos (demais IDs)
                elif current_category:
                    current_category['subprodutos'].append({
                        'produto': row['produto'].strip(),
                        'quantidade': parse_quantity(row[year_str])
                    })

            # Calcula o total somando as categorias principais
            total = sum(item['quantidade'] for item in data if item['quantidade'])
            
            return {
                'ano': year,
                'dados': data,
                'total': total
            }
            
    except Exception as e:
        print(f'Erro ao processar CSV: {str(e)}')
        return None
    
def convert_decimal(obj):
    if isinstance(obj, decimal.Decimal):
        return float(obj)
    raise TypeError(f"Object of type {type(obj).__name__} is not JSON serializable")

@app.route('/api/producao', methods=['GET'])
def get_production():
    """
    Consulta dados de produção vitivinícola
    ---
    tags:
      - Produção
    parameters:
      - name: ano
        in: query
        type: integer
        required: false
        default: 2023
        minimum: 1970
        maximum: 2023
        description: Ano da produção (1970-2023)
    responses:
      200:
        description: Dados de produção encontrados
        content:
          application/json:
            schema:
              $ref: '#/components/schemas/Producao'
            examples:
              exemplo:
                value: {
                  "ano": 2023,
                  "dados": [
                    {
                      "produto": "VINHO DE MESA",
                      "quantidade": 169762429,
                      "subprodutos": [
                        {"produto": "Tinto", "quantidade": 139320884},
                        {"produto": "Branco", "quantidade": 27910299}
                      ]
                    }
                  ],
                  "total": 457792870
                }
      400:
        description: Ano inválido fornecido
      503:
        description: Dados indisponíveis
    """
    year = request.args.get('ano', default=2023, type=int)
    
    # Validação do ano
    if year < 1970 or year > 2023:
        return jsonify({'erro': 'Ano inválido'}), 400

    # 1. Verifica cache
    cache_key = f"producao:{year}"
    if cached := redis_client.get(cache_key):
        return jsonify(json.loads(cached))

    # 2. Tenta banco de dados
    if db_data := get_from_database(year):
        try:
            db_data_json = json.dumps(db_data, default=str) # Usar default=str para decimais
            redis_client.setex(cache_key, 3600, db_data_json)
            return jsonify(db_data) # Flask pode lidar com Decimal se configurado, mas jsonify pode falhar
        except TypeError:
             # Fallback ou log de erro
             return jsonify(json.loads(json.dumps(db_data, default=str))) # Re-serializa

    # 3. Fallback para scraping
    try:
        scraped_data = scrape_production(year)
        if scraped_data:
            backup_path = os.path.join(BACKUP_DIR, f'producao_{year}.json')
            try:
                with open(backup_path, 'w', encoding='utf-8') as f:
                    json.dump(scraped_data, f, ensure_ascii=False, indent=2)
                logging.info(f"Backup salvo em: {backup_path}")
            except Exception as e:
                logging.error(f"Erro ao salvar JSON: {str(e)}")
            try:
                if save_to_database(scraped_data):
                    logging.info("Dados salvos no PostgreSQL")
                    # Precisa definir a função convert_decimal ou usar json.dumps com default=str
                    try:
                       scraped_data_json = json.dumps(scraped_data, default=str)
                       redis_client.setex(cache_key, 3600, scraped_data_json)
                       return jsonify(scraped_data)
                    except TypeError:
                        return jsonify(json.loads(json.dumps(scraped_data, default=str)))
                else:
                    logging.warning("Falha ao salvar no PostgreSQL")
            except Exception as e:
                logging.error(f"Erro crítico no PostgreSQL: {str(e)}")
                # Retornar o dado raspado mesmo se falhar no DB?
                return jsonify(scraped_data) # Ou retornar erro?
    except Exception as e:
        logging.error(f"Erro no scraping: {str(e)}")

    backup_data = load_backup(year)
    if backup_data:
        return jsonify(backup_data)
    
    return jsonify({'erro': 'Dados indisponíveis'}), 503

def create_tables():
    try:
        with app.app_context():
            db.create_all()
            print("✅ Tabelas criadas/verificadas com sucesso.")
    except Exception as e:
        print(f"❌ Erro ao criar tabelas: {e}")

if __name__ == '__main__':
    create_tables()
    app.run(debug=True, host='0.0.0.0',  port=5000)
