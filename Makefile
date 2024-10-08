all:
	@echo "make certs - generate certs"
	@echo "make test - run tests"
	@echo "make build - build the project"
	@echo "make start - start the server"
	@echo "make up - start the ssl proxy in docker"
	@echo "make down - stop the server in docker"
	@echo "make enable-net - enable network binding for the server"
	@echo "make clean - clean the project"

certs:
	@openssl req -x509 -extensions v3_req -config data/mcouniverse.cnf -newkey rsa:1024 -nodes -keyout ./data/private_key.pem -out ./data/mcouniverse.pem -days 365
	@openssl rsa -in ./data/private_key.pem -outform DER -pubout | xxd -ps -c 300 | tr -d '\n' > ./data/pub.key
	@cp ./data/mcouniverse.pem  ./data/private_key.pem ./services/sslProxy/
	@echo "certs regenerated. remember to update pub.key for all clients"

lint:
	# stop the build if there are Python syntax errors or undefined names
	@pdm run flake8 pyrace --count --select=E9,F63,F7,F82 --show-source --statistics
	# exit-zero treats all errors as warnings. The GitHub editor is 127 chars wide
	@pdm run flake8 pyrace --count --exit-zero --max-complexity=10 --max-line-length=127 --statistics


test:
	@pdm run pytest --cov=pyrace --cov-report=term-missing && pdm run python -m coverage xml

install:
	@pdm install

start:
	@python main.py

start-web:
	@python web/manage.py runserver 0.0.0.0:3000

up:
	docker-compose up -d --build

down:
	docker-compose down

enable-net:
	@sudo setcap cap_net_bind_service=+ep ./target/debug/rusty_server

clean:
	@cargo clean

.PHONY: all certs test build start up down enable-net clean lint