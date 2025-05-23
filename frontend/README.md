# README para o Frontend

## Frontend - Aplicação Next.js com Tailwind CSS

Esta pasta contém a aplicação frontend desenvolvida com Next.js e estilizada com Tailwind CSS.

### Tecnologias Utilizadas

- Next.js 15.3.2
- React 19
- Tailwind CSS 3.3.0
- TypeScript

### Estrutura de Arquivos

```
frontend/
├── app/                  # Diretório principal do App Router
│   ├── components/       # Componentes reutilizáveis
│   ├── globals.css       # Estilos globais com Tailwind
│   ├── layout.tsx        # Layout principal da aplicação
│   └── page.js           # Página inicial
├── public/               # Arquivos estáticos
├── .env.local            # Variáveis de ambiente locais
├── next.config.js        # Configuração do Next.js
├── package.json          # Dependências e scripts
├── postcss.config.js     # Configuração do PostCSS
└── tailwind.config.js    # Configuração do Tailwind CSS
```

### Instalação

```bash
# Instalar dependências
npm install

# Executar em modo de desenvolvimento
npm run dev

# Construir para produção
npm run build

# Iniciar em modo de produção
npm run start
```

### Variáveis de Ambiente

Crie um arquivo `.env.local` na raiz do diretório frontend com as seguintes variáveis:

```
NEXT_PUBLIC_API_URL=http://localhost:5000
```

### Componentes Principais

- **Producao.js**: Componente para exibição dos dados de produção vitivinícola

### Rotas Disponíveis

- `/`: Página inicial com consulta de produção
- `/about`: Página sobre o projeto
