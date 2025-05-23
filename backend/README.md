# README para o Backend

## Backend - API Embrapa

Esta pasta contém a API backend que fornece acesso aos dados de produção vitivinícola.

### Tecnologias Utilizadas

- Node.js
- Express.js
- Banco de dados (especificar qual banco está sendo usado)

### Estrutura de Arquivos

```
backend/
├── src/                  # Código-fonte da API
│   ├── controllers/      # Controladores da API
│   ├── models/           # Modelos de dados
│   ├── routes/           # Definição de rotas
│   └── index.js          # Ponto de entrada da aplicação
├── tests/                # Testes automatizados
├── .env                  # Variáveis de ambiente (não versionado)
└── package.json          # Dependências e scripts
```

### Instalação

```bash
# Instalar dependências
npm install

# Executar em modo de desenvolvimento
npm run dev

# Executar testes
npm test

# Iniciar em modo de produção
npm start
```

### Variáveis de Ambiente

Crie um arquivo `.env` na raiz do diretório backend com as seguintes variáveis:

```
PORT=5000
DB_CONNECTION_STRING=sua_string_de_conexao
```

### Endpoints da API

- `GET /api/producao?ano=XXXX`: Retorna dados de produção para o ano especificado
- (Adicionar outros endpoints conforme necessário)

### Autenticação

(Descrever o método de autenticação, se aplicável)

### Logs e Monitoramento

(Descrever como os logs são gerenciados e como monitorar a API)
