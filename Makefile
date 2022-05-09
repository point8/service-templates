init: setup_docker_networks set_domain_name set_service_name

setup_docker_networks:
	docker network create web
	docker network create --internal local

set_domain_name:
	sed -i -- 's/DOMAIN_PLACEHOLDER/$(shell cat CNAME)/g' Caddyfile

set_service_name:
	sed -i -- 's/SERVICE_PLACEHOLDER/$(shell cat SERVICE)/g' Caddyfile
