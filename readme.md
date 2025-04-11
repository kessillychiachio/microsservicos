# 🌿 Sistema de Aromaterapia com Microsserviços

Este projeto implementa uma arquitetura de microsserviços em Python com FastAPI, Docker e SQLite para gerenciar um sistema de aromaterapia. Cada serviço é responsável por uma parte da lógica do domínio, e são orquestrados por um cliente que interage com todos eles.

## 📦 Estrutura dos Microsserviços

```
.
├── catalogo/              # Cadastro de óleos essenciais
├── recomendar/            # Sugestões de óleos por sintomas
├── misturas/              # Criação e validação de misturas
├── contraindicacoes/      # Regras de segurança por perfil
├── cliente/               # Script consumidor de todos os serviços
├── docker-compose.yml     # Orquestração dos serviços
├── .env                   # Configurações de portas
└── Makefile               # Comandos utilitários para dev
```

---

## 🚀 Como rodar tudo

### Pré-requisitos:
- Docker
- Docker Compose

### 1. Clone o projeto
```bash
git clone https://github.com/kessillychiachio/microsservicos.git
cd microsservicos
```

### 2. Rode tudo com Docker Compose
```bash
docker-compose up --build
```

---

## 🌐 Endpoints disponíveis

| Serviço           | URL                         | Porta  |
|-------------------|------------------------------|--------|
| Catálogo          | `http://localhost:5011/docs` | 5011   |
| Recomendar        | `http://localhost:5012/docs` | 5012   |
| Misturas          | `http://localhost:5013/docs` | 5013   |
| Contraindicações  | `http://localhost:5014/docs` | 5014   |

> O cliente roda internamente no container e simula chamadas automáticas.

---

## 🧠 Microsserviços independentes

Todos os serviços são autônomos, com banco de dados local (`SQLite`) e podem ser executados separadamente:

```bash
docker-compose up catalogo
docker-compose up recomendar
docker-compose up misturas
docker-compose up contraindicacoes
```

---

## 🛠️ Automatizando com `Makefile`

Este projeto inclui um `Makefile` com comandos curtos e padronizados para facilitar a execução do Docker Compose. Isso evita que você precise lembrar comandos longos e garante consistência no desenvolvimento.

### Comandos disponíveis:

```bash
make up        # Sobe todos os serviços com build
make stop      # Para todos os containers
make down      # Para e remove containers
make rebuild   # Derruba tudo e sobe do zero
make logs      # Ver os logs em tempo real
make ps        # Ver o status dos serviços
```

> 💡 Certifique-se de ter o `make` instalado no seu sistema (já vem por padrão no Linux/macOS).

---

## 🧪 Testando a aplicação

O serviço `cliente` executa automaticamente, realizando chamadas REST periódicas para:

- Obter óleos cadastrados
- Recomendar óleos para sintomas
- Criar e listar misturas
- Verificar contraindicações
- Testar alterações (`PUT`) e exclusões (`DELETE`)

Você pode acompanhar tudo no terminal com:

```bash
docker-compose logs -f cliente
```

---

## ✨ Tecnologias utilizadas

- [FastAPI](https://fastapi.tiangolo.com/)
- [Docker](https://www.docker.com/)
- [SQLite](https://www.sqlite.org/)
- [SQLAlchemy](https://www.sqlalchemy.org/)
- [Python 3.11+](https://www.python.org/)

---

## 📫 Testando com Postman

Este repositório inclui uma coleção do Postman para facilitar o teste de todos os microsserviços.

Para usar:

1. Abra o Postman
2. Clique em **Import**
3. Selecione o arquivo `.postman_collection.json`
4. Teste os endpoints locais em: `http://localhost:5011`, `5012`, etc.

---

## 📃 Licença

Projeto para fins acadêmicos (curso de Pós-graduação em Desenvolvimento Web | IFBA). Uso livre para estudos e demonstrações.

---