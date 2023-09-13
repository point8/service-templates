# Alpine JS

Website: [alpinejs.dev/](https://alpinejs.dev/)

Everything is located in the `alpinejs/` directory. Feel free to add your own code.

Please note: the current minimal example is build around a [PocketBase](pocketbase.md) backend!

## Dockerfile

The docker image only handles the static assets and the generated container then sleeps infinitely. See below how you can tell Caddy to serve those static assets.

## docker-compose

Add the following configuration block as a service to the `compose.yaml` file:

```yaml
  alpinejs:
    build:
      context: services/alpinejs
    restart: unless-stopped
    volumes:
      - alpinejs-app:/app
    networks:
      - local
```

Change the `depends_on` value of the `caddy` service to `alpinejs`.

As the caddy service should serve your static assets, you need to mount the files into a docker volume and share this volume with the caddy service.

```
volumes:
  - ./Caddyfile:/etc/caddy/Caddyfile
  - caddy-data:/data
  - caddy-config:/config
  - alpinejs-app:/app
```

And declare the volume at the end of the compose file

```
volumes:
  ...
  alpinejs-app:
```

## Caddyfile

To serve all HTTPs requests with the static assets change the reverse proxy line in the `Caddyfile` to:
```
file_server {
    root /app
}
```
