Sistema de Microsserviços: Óleos Essenciais

Visão Geral

Este sistema foi desenvolvido para a disciplina de Desenvolvimento de Aplicações Orientadas a Serviços com base no paradigma de microsserviços web conteinerizados, conforme os requisitos da atividade.

Ele é composto por quatro microsserviços independentes e um cliente automático que consome todos os serviços de forma contínua, mesmo em caso de falhas.

Arquitetura da Solução

Cada serviço está em um contêiner Docker isolado.
Comunicação via HTTP entre os serviços.
Cliente assíncrono com requests e time.sleep().
Orquestração com docker-compose.

Microsserviços:

catalogo: Lista óleos essenciais com seus benefícios
recomendar: Sugere óleos com base em sintomas informados
misturas: Cria e lista misturas personalizadas, impedindo combinações antagônicas
contraindicacoes: Verifica óleos não recomendados para perfis específicos (gravidez etc)
cliente: Consome todos os serviços automaticamente (main.py)

Como Executar:

Suba os serviços com Docker Compose:
docker compose up --build
O cliente (main.py) começa automaticamente a consultar todos os microsserviços e exibir os resultados no terminal.


Fluxo de Execução do Cliente:

A cada 5 segundos, o cliente realiza:

Consulta ao /oleos (catálogo)
Requisição POST para /recomendar (recomendações por sintomas)
Criação de mistura com POST /misturas
Listagem de misturas com GET /misturas
Verificação de contraindicações com POST /verificar

Estrutura de Pastas:

microsservicos/
├── catalogo/
│   └── app.py
    ├── requirements.txt
│   └── Dockerfile
├── recomendar/
│   └── app.py
    ├── requirements.txt
│   └── Dockerfile
├── misturas/
│   └── app.py
    ├── requirements.txt
│   └── Dockerfile
├── contraindicacoes/
│   └── app.py
    ├── requirements.txt
│   └── Dockerfile
├── contraindicacoes/
│   └── app.py
    ├── requirements.txt
│   └── Dockerfile
├── cliente/
│   ├── main.py
│   ├── requirements.txt
│   └── Dockerfile
└── docker-compose.yaml
