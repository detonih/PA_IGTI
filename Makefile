build:
	docker build -t big-data-plataform .

up:
	docker-compose up

bash:
	docker exec -it big-data-plataform /bin/bash

prune:
	docker stop big-data-plataform 
	docker container prune