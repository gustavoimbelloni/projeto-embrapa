# README para o Frontend (Next.js)

## Frontend - Aplicação de Consulta Embrapa

Esta pasta contém a aplicação frontend desenvolvida com Next.js e estilizada com Tailwind CSS. Ela consome a API backend para exibir os dados de produção vitivinícola.

### Tecnologias Utilizadas

- Next.js 15.x (com App Router)
- React 19
- Tailwind CSS 3.x
- TypeScript

### Estrutura de Arquivos

```
frontend/
├── app/                  # Diretório principal do App Router
│   ├── components/       # Componentes reutilizáveis (ex: Producao.js)
│   ├── globals.css       # Estilos globais com Tailwind
│   ├── layout.tsx        # Layout principal da aplicação
│   └── page.js           # Página inicial
├── public/               # Arquivos estáticos (ex: favicon.ico)
├── .env.local            # Variáveis de ambiente LOCAIS (NÃO VERSIONAR)
├── next.config.js        # Configuração do Next.js
├── package.json          # Dependências e scripts npm
├── Dockerfile            # Instruções para build da imagem Docker
├── postcss.config.js     # Configuração do PostCSS (para Tailwind)
└── tailwind.config.js    # Configuração do Tailwind CSS
└── README.md             # Esta documentação
```

### Instalação e Configuração (Desenvolvimento Local)

1.  **Navegue até a pasta**:
    ```bash
    cd frontend
    ```

2.  **Instale as dependências**:
    ```bash
    npm install
    ```

3.  **Configure as Variáveis de Ambiente Locais**:
    Crie um arquivo `.env.local` na raiz do `frontend`:
    ```dotenv
    # URL da API Backend rodando localmente (ou via Docker na porta mapeada)
    NEXT_PUBLIC_API_URL=http://localhost:5000
    ```
    *Lembre-se de adicionar `.env.local` ao `.gitignore`.*

4.  **Garanta que a API Backend esteja rodando** (localmente ou via Docker na porta 5000).

### Execução (Desenvolvimento Local)

Com a API rodando, inicie o servidor de desenvolvimento do Next.js:

```bash
npm run dev
```
A aplicação estará disponível em [http://localhost:3001](http://localhost:3001) (ou outra porta indicada).

### Execução com Docker Compose

Consulte o `README.md` principal na raiz do projeto para instruções sobre como executar todo o sistema (incluindo este frontend) usando `docker-compose up`.

A variável de ambiente `NEXT_PUBLIC_API_URL` para o container é definida diretamente no `docker-compose.yml` (ex: `NEXT_PUBLIC_API_URL=http://api:5000`), garantindo a comunicação com o backend dentro da rede Docker.

### Build para Produção

Para gerar os arquivos otimizados para produção:

```bash
npm run build
```

Para iniciar o servidor de produção (após o build):

```bash
npm run start
```

### Componentes e Páginas Principais

-   **`app/page.js`**: Página inicial que provavelmente utiliza o componente de consulta.
-   **`app/components/Producao.js`**: Componente responsável por buscar e exibir os dados da API.
-   **`app/layout.tsx`**: Define a estrutura HTML base e importa os estilos globais.

