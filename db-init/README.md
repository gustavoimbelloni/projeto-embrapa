# README para o Banco de Dados (PostgreSQL)

## Configuração do Banco de Dados

Esta pasta contém configurações e scripts relacionados ao banco de dados PostgreSQL utilizado pelo backend.

### Estrutura

```
db-init/
|  └── init.sql  # Script SQL para criação inicial do schema (tabelas)
└── README.md     # Esta documentação
```

### Script de Inicialização (`db-init/init.sql`)

-   Este diretório (`db-init`) contém scripts SQL (`.sql`) que são executados automaticamente pelo container oficial do PostgreSQL na **primeira vez** que ele é inicializado com um volume de dados vazio.
-   O arquivo `init.sql` (ou qualquer arquivo `.sql` nesta pasta) é usado para criar as tabelas necessárias para a aplicação, como a tabela `producao`.
-   **Importante**: Se o volume de dados do PostgreSQL (`pgdata` no `docker-compose.yml`) já existir de execuções anteriores, esses scripts **não** serão executados novamente. Para forçar a execução (recriando o banco do zero), você precisa parar os containers (`docker-compose down`) e remover o volume (`docker volume rm projeto-embrapa_pgdata`) antes de iniciar novamente (`docker-compose up`).

### Configuração no Docker Compose

O serviço `embrapa-db` no arquivo `docker-compose.yml` na raiz do projeto define como o container do PostgreSQL é configurado:

```yaml
services:
  # ... (outros serviços)
  embrapa-db:
    image: postgres:13
    environment:
      POSTGRES_USER: user
      POSTGRES_PASSWORD: password
      POSTGRES_DB: vitivinicultura
    volumes:
      - pgdata:/var/lib/postgresql/data # Volume persistente para os dados
      - ./db-init:/docker-entrypoint-initdb.d # Mapeia os scripts de init
    ports:
      - "5432:5432"
# ... (definição do volume pgdata)
```

-   As variáveis de ambiente definem o usuário, senha e nome do banco de dados inicial.
-   O volume `pgdata` garante que os dados persistam entre reinicializações dos containers.
-   O volume que mapeia `./db-init` para `/docker-entrypoint-initdb.d` é o que permite a execução automática dos scripts SQL na primeira inicialização.

### Acesso ao Banco de Dados

-   A API Flask se conecta ao banco de dados usando a URL definida na variável de ambiente `DATABASE_URL` (ex: `postgresql://user:password@embrapa-db:5432/vitivinicultura`). Note que dentro da rede Docker, o hostname é o nome do serviço (`embrapa-db`).
-   Para acesso externo (ex: usando uma ferramenta como DBeaver ou pgAdmin na sua máquina local), você pode se conectar a `localhost:5432` usando as credenciais definidas.

