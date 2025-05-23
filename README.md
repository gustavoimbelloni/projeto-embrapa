# Projeto Embrapa

Este repositório contém o sistema completo de consulta de produção vitivinícola, incluindo frontend, backend, configuração de banco de dados e ferramentas de backup.

## Estrutura do Projeto

- **frontend/**: Aplicação Next.js com Tailwind CSS
- **backend/**: API REST desenvolvida para acesso aos dados
- **database/**: Scripts de inicialização e configuração do banco de dados
- **data/**: Armazenamento de backups e dados de consulta

## Requisitos

- Node.js 18+
- Docker e Docker Compose
- Git

## Instalação e Execução

### Usando Docker (Recomendado)

1. Clone o repositório:
```bash
git clone https://github.com/seu-usuario/projeto-embrapa.git
cd projeto-embrapa
```

2. Inicie os containers:
```bash
docker-compose up -d
```

3. Acesse a aplicação:
   - Frontend: http://localhost:3001
   - API: http://localhost:5000

### Instalação Manual

#### Backend
```bash
cd backend
npm install
npm run dev
```

#### Frontend
```bash
cd frontend
npm install
npm run dev
```

## Documentação

- [Documentação do Frontend](./frontend/README.md)
- [Documentação do Backend](./backend/README.md)
- [Configuração do Banco de Dados](./database/README.md)

## Contribuição

1. Faça um fork do projeto
2. Crie uma branch para sua feature (`git checkout -b feature/nova-funcionalidade`)
3. Commit suas mudanças (`git commit -m 'Adiciona nova funcionalidade'`)
4. Push para a branch (`git push origin feature/nova-funcionalidade`)
5. Abra um Pull Request

## Licença

Este projeto está licenciado sob a licença [inserir licença].
