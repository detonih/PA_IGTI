build:
	docker build -t big-data-plataform .

build-web:
	docker build -t web-frontend .

up:
	docker-compose up --build

bash:
	docker exec -it big-data-plataform /bin/bash

prune:
	docker stop big-data-plataform 
	docker stop web-frontend 
	docker container prune