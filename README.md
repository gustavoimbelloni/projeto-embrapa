# Projeto Embrapa - Consulta de Produção Vitivinícola

Este repositório contém o sistema completo para consulta de dados de produção vitivinícola da Embrapa, utilizando web scraping, API REST, banco de dados e uma interface web interativa. O projeto é totalmente containerizado usando Docker e Docker Compose para facilitar a configuração e execução do ambiente.

## Estrutura do Projeto

```
projeto-embrapa/
├── backend/              # API Flask (Python) e App Streamlit
│   ├── src/
│   ├── static/
│   ├── .env              # (Exemplo, não versionar)
│   ├── requirements.txt
│   └── README.md
├── frontend/             # Aplicação Next.js com Tailwind CSS
│   ├── app/
│   ├── public/
│   ├── .env.local        # (Exemplo, não versionar)
│   ├── package.json
│   ├── Dockerfile
│   └── README.md
├── database/    
├── db-init/
│    └── init.sql         # Scripts SQL para inicialização do DB
├── data/
│   └── backup/           # Backups de dados (ex: JSON, CSV)
├── .gitignore            # Arquivos e pastas a serem ignorados pelo Git
├── docker-compose.yml    # Orquestração dos containers Docker
└── README.md             # Este arquivo
```

## Tecnologias Utilizadas

- **Frontend**: Next.js, React, Tailwind CSS, TypeScript
- **Backend**: Python, Flask, SQLAlchemy, Streamlit, Pandas, Requests, BeautifulSoup4, Redis, Psycopg2
- **Banco de Dados**: PostgreSQL
- **Containerização**: Docker, Docker Compose
- **Versionamento**: Git, GitHub

## Pré-requisitos

- Git
- Docker
- Docker Compose (geralmente incluído na instalação do Docker Desktop)
- Node.js e npm (apenas para desenvolvimento local do frontend)
- Python e pip (apenas para desenvolvimento local do backend)

## Instalação e Execução (Docker Compose - Recomendado)

1.  **Clone o repositório**:
    ```bash
    git clone https://github.com/gustavoimbelloni/projeto-embrapa.git
    cd projeto-embrapa
    ```

2.  **Configure as Variáveis de Ambiente (Opcional - Padrões Definidos)**:
    *   O `docker-compose.yml` já define as variáveis necessárias para os containers se comunicarem (como `NEXT_PUBLIC_API_URL`, `DATABASE_URL`, `REDIS_HOST`).
    *   Se precisar ajustar senhas ou portas padrão, edite o `docker-compose.yml` ou crie arquivos `.env` nas pastas `backend` e `frontend` (consulte os READMEs específicos para detalhes, mas lembre-se que as variáveis no `docker-compose.yml` têm precedência no ambiente Docker).

3.  **Construa e Inicie os Containers**:
    ```bash
    docker-compose up --build -d
    ```
    *   `--build`: Força a reconstrução das imagens se houver alterações nos Dockerfiles.
    *   `-d`: Executa os containers em segundo plano (detached mode).

4.  **Acesse as Aplicações**:
    *   **Frontend**: [http://localhost:3001](http://localhost:3001)
    *   **API (Documentação Swagger)**: [http://localhost:5000/api/docs/](http://localhost:5000/api/docs/)
    *   **Dashboard Streamlit** (se estiver rodando): Verifique os logs do backend ou execute manualmente.

5.  **Parar os Containers**:
    ```bash
    docker-compose down
    ```

## Desenvolvimento Local (Sem Docker)

Consulte os arquivos README específicos dentro das pastas `frontend` e `backend` para instruções detalhadas sobre como configurar e executar cada parte localmente.

## Documentação Específica

- [README do Frontend](./frontend/README.md)
- [README do Backend](./backend/README.md)
- [README do Banco de Dados](./db-init/README.md)

## Contribuição

1.  Faça um fork do projeto.
2.  Crie uma branch para sua feature (`git checkout -b feature/nova-funcionalidade`).
3.  Faça commit das suas mudanças (`git commit -m 'Adiciona nova funcionalidade'`).
4.  Faça push para a branch (`git push origin feature/nova-funcionalidade`).
5.  Abra um Pull Request.

## Licença

(Defina a licença do seu projeto aqui, por exemplo: MIT License)

