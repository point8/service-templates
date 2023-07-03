# Voilà

Website: [voila.readthedocs.io/](https://voila.readthedocs.io/)

Everything is located in the `voila/` directory. Feel free to add your own code. A basic app can be found in `voila/example.ipynb`.

## Dockerfile

To change the command running the app, you need to adapt the last line in the `Dockerfile` to reflect those changes:

```
CMD ["poetry", "run", "voila", "--no-browser", "--Voila.ip='0.0.0.0'", "--port=8866", "example.ipynb"]
```

If you remove the last part (`"example.ipynb"`), the user gets a list of all available notebooks.

## docker-compose

Add the following configuration block as a service to the `compose.yaml` file:

```yaml
voila:
  build:
    context: services/voila
  restart: unless-stopped
  expose:
    - 8866
  networks:
    - local
  depends_on:
    - postgres
    - mongodb
    - redis
```

## Caddyfile

To redirect all external HTTPs requests to the service change the reverse proxy line in the `Caddyfile` to:

```
reverse_proxy voila:8866
```
