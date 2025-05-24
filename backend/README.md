# README para o Backend (Python/Flask)

## Backend - API Embrapa (Python/Flask)

Esta pasta contém a API backend desenvolvida em Python com o framework Flask, responsável por fornecer acesso aos dados de produção vitivinícola.

### Tecnologias Utilizadas

- Python 3.x
- Flask (>=2.0)
- Flask-SQLAlchemy (para interação com banco de dados)
- Flask-CORS (para habilitar Cross-Origin Resource Sharing)
- Flask-Swagger-UI (para documentação interativa da API)
- SQLAlchemy
- Psycopg2 (para conexão com PostgreSQL)
- Redis (para caching ou outras funcionalidades)
- Requests (para fazer requisições HTTP)
- BeautifulSoup4 (para web scraping, se aplicável)
- python-dotenv (para gerenciamento de variáveis de ambiente)

### Estrutura de Arquivos (Exemplo)

```
backend/
├── src/                  # Código-fonte da API
│   ├── controllers/      # Lógica de negócio e endpoints
│   ├── models/           # Modelos SQLAlchemy
│   ├── services/         # Serviços auxiliares
│   ├── utils/            # Funções utilitárias
│   └── app.py            # Ponto de entrada da aplicação Flask
├── tests/                # Testes automatizados
├── .env                  # Variáveis de ambiente (não versionado)
├── requirements.txt      # Dependências Python
└── README.md             # Esta documentação
```

### Instalação e Configuração

1.  **Clone o repositório** (se ainda não o fez):
    ```bash
    git clone https://github.com/gustavoimbelloni/projeto-embrapa.git
    cd projeto-embrapa/backend
    ```

2.  **Crie e ative um ambiente virtual** (recomendado):
    ```bash
    # Criar ambiente virtual
    python -m venv .venv

    # Ativar no Windows
    .venv\Scripts\activate

    # Ativar no Linux/Mac
    source .venv/bin/activate
    ```

3.  **Instale as dependências**:
    ```bash
    pip install -r requirements.txt
    ```

4.  **Configure as Variáveis de Ambiente**:
    Crie um arquivo `.env` na raiz do diretório `backend` com as seguintes variáveis (ajuste os valores conforme seu ambiente):
    ```dotenv
    FLASK_APP=src/app.py
    FLASK_ENV=development # ou production
    DATABASE_URL=postgresql://usuario:senha@host:porta/nome_banco
    REDIS_URL=redis://host:porta
    # Adicione outras variáveis necessárias (chaves de API, etc.)
    ```
    *Certifique-se de adicionar `.env` ao seu arquivo `.gitignore` principal.*

### Execução

1.  **Inicie o servidor Flask**:
    Com o ambiente virtual ativado e as variáveis de ambiente configuradas:
    ```bash
    flask run
    ```
    A API estará disponível por padrão em `http://127.0.0.1:5000` (ou na porta definida no seu `.env` ou configuração Docker).

### Documentação da API (Swagger UI)

Se configurado, a documentação interativa da API pode ser acessada em:
`http://127.0.0.1:5000/api/docs` (verifique a rota exata na configuração do `flask-swagger-ui`).

### Endpoints Principais (Exemplo)

- `GET /api/producao?ano=XXXX`: Retorna dados de produção para o ano especificado.
- (Adicione outros endpoints conforme implementado).

### Testes

(Descreva como executar os testes, se houver)
```bash
# Exemplo: pytest
pytest
```
