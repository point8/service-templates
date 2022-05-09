init: init_domain_name init_service_name

init_docker_networks:
	docker network create web
	docker network create --internal local

init_domain_name:
	sed -i -- 's/DOMAIN_PLACEHOLDER/$(shell cat CNAME)/g' Caddyfile
	rm Caddyfile--

init_service_name:
	sed -i -- 's/SERVICE_PLACEHOLDER/$(shell cat SERVICE)/g' Caddyfile
	rm Caddyfile--

deploy:
	scp -r $(shell cat SERVICE) Caddyfile docker-compose.yml $(shell cat CNAME):
	-ssh $(shell cat CNAME) 'docker network create web'
	-ssh $(shell cat CNAME) 'docker network create --internal local'
	ssh $(shell cat CNAME) 'docker-compose up'
