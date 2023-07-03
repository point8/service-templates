# Svelte

Website: [svelte.dev](https://svelte.dev)

Everything is located in the `svelte/` directory. Feel free to add your own code.

## Dockerfile

To change the command running the app, you need to adapt the last line in the `Dockerfile` to reflect those changes:

```
CMD ["build"]
```

The entrypoint of this image is set to `node`, so this image expects users to supply a path to e.g. a .`js` file in the `CMD`.

## docker-compose

Add the following configuration block as a service to the `compose.yaml` file:

```yaml
svelte:
  build:
    context: services/svelte
  restart: unless-stopped
  expose:
    - 3000
  networks:
    - local
  depends_on:
    - postgres
    - mongodb
    - redis
```

Adapt the given `depends_on` values to your needs. Also change the `depends_on` value of the `caddy` service to `svelte`.

## Caddyfile

To redirect all external HTTPs requests to the service change the reverse proxy line in the `Caddyfile` to:

```
reverse_proxy svelte:3000
```
