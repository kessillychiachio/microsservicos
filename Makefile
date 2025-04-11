# Caminho padrão para o compose
COMPOSE=docker-compose --env-file .env

# Sobe todos os microsserviços
up:
	$(COMPOSE) up --build

# Para os containers
stop:
	$(COMPOSE) stop

# Derruba e remove os containers (sem perder as imagens)
down:
	$(COMPOSE) down

# Verifica os logs de todos os serviços
logs:
	$(COMPOSE) logs -f

# Rebuild total
rebuild:
	$(COMPOSE) down
	$(COMPOSE) up --build

# Verifica status
ps:
	$(COMPOSE) ps
