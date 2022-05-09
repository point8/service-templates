init: init_docker_networks init_domain_name init_service_name

init_docker_networks:
	docker network create web
	docker network create --internal local

init_domain_name:
	sed -i -- 's/DOMAIN_PLACEHOLDER/$(shell cat CNAME)/g' Caddyfile

init_service_name:
	sed -i -- 's/SERVICE_PLACEHOLDER/$(shell cat SERVICE)/g' Caddyfile
