# README para o Backend (Python: API Flask + App Streamlit)

## Backend - API Embrapa e Dashboard de Consulta

Esta pasta contém o backend do projeto, composto por duas aplicações Python:

1.  **API Flask**: Fornece endpoints RESTful para acesso aos dados de produção vitivinícola, com scraping, cache Redis e persistência em PostgreSQL.
2.  **Aplicação Streamlit**: Um dashboard interativo (`src/app.py`) para visualização e consulta dos dados (provavelmente consumindo a API Flask).

### Tecnologias Utilizadas

- Python 3.x
- **API**: Flask, Flask-SQLAlchemy, Flask-CORS, Flask-Swagger-UI, SQLAlchemy, Psycopg2, python-dotenv, Redis
- **Dashboard**: Streamlit, Pandas, Requests
- **Comum**: Requests, BeautifulSoup4

### Estrutura de Arquivos

```
backend/
├── src/
│   ├── api/                # (Opcional) Código da API Flask
│   │   └── main.py         # Ponto de entrada da API (ou app_flask.py)
│   ├   └── app.py          # Ponto de entrada do Dashboard     
│   │   └── database.py
│   │   └── models.py
├── static/                 # Arquivos estáticos (servidos pelo Flask)
│   └── swagger.json
├── tests/
├── .env                  # Variáveis de ambiente para DEV LOCAL (NÃO VERSIONAR)
├── requirements.txt      # Dependências Python (Flask, Streamlit, etc.)
└── README.md             # Esta documentação
```
*(Ajuste os nomes e a estrutura conforme seu projeto real. O Flask está configurado para servir arquivos da pasta `backend/static` na URL `/static`)*

### Instalação e Configuração (Desenvolvimento Local)

1.  **Navegue até a pasta**:
    ```bash
    cd backend
    ```

2.  **Crie e ative um ambiente virtual**:
    ```bash
    python -m venv .venv
    # Windows: .venv\Scripts\activate
    # Linux/Mac: source .venv/bin/activate
    ```

3.  **Instale as dependências**:
    *Certifique-se de que `requirements.txt` está atualizado.*
    ```bash
    pip install -r requirements.txt
    ```

4.  **Configure as Variáveis de Ambiente Locais**:
    Crie um arquivo `.env` na raiz do `backend` (copie de `.env.example` se existir):
    ```dotenv
    # Para a API Flask
    FLASK_APP=src/main.py # Ajuste o caminho
    FLASK_ENV=development
    # Conexão com DB e Redis rodando localmente ou via Docker
    DATABASE_URL=postgresql://user:password@localhost:5432/vitivinicultura
    REDIS_URL=redis://localhost:6379

    # Para o App Streamlit (se ele consumir a API)
    API_BASE_URL=http://localhost:5000
    ```
    *Lembre-se de adicionar `.env` ao `.gitignore`.*

5.  **Prepare o Arquivo de Documentação da API**:
    Certifique-se de que o arquivo `swagger.json` esteja em `backend/static/swagger.json`.

6.  **Garanta que DB e Redis estejam rodando** (localmente ou via Docker Compose separado).

### Execução (Desenvolvimento Local)

Execute a API Flask e o App Streamlit separadamente em terminais diferentes (com o ambiente virtual ativado):

1.  **Inicie a API Flask**:
    ```bash
    flask run --host=0.0.0.0 --port=5000
    ```

2.  **Inicie o App Streamlit**:
    ```bash
    streamlit run src/app.py 
    ```

### Execução com Docker Compose

Consulte o `README.md` principal na raiz do projeto para instruções sobre como executar todo o sistema (incluindo este backend) usando `docker-compose up`.

As variáveis de ambiente para o container são definidas diretamente no `docker-compose.yml` (ex: `FLASK_APP=src/main.py`, `REDIS_HOST=embrapa-cache`).

### Endpoints Principais da API Flask

- `GET /`: Rota raiz, retorna uma mensagem de boas-vindas.
- `GET /api/producao?ano=XXXX`: Retorna dados de produção para o ano especificado.
- `GET /static/<filename>`: Serve arquivos estáticos da pasta `backend/static`.

### Documentação da API (Swagger UI)

Quando rodando (localmente ou via Docker), acesse a documentação interativa em:
`http://localhost:5000/api/docs/`

### Testes

(Descreva como executar os testes, se houver)

