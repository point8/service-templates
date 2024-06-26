# Marimo

Website: [marimo.io](https://marimo.io/)

Everything is located in the `marimo/` directory. Feel free to add your own code. A basic app can be found in `marimo/notebook.py`.

## Dockerfile

To change the command running the app, you need to adapt the last line in the `Dockerfile` to reflect those changes:

```
CMD ["poetry", "run", "marimo", "run", "notebook.py", "--host", "0.0.0.0", "--port", "8080", "--headless"]
```

## docker-compose

Add the following configuration block as a service to the `compose.yaml` file:

```yaml
marimo:
  build:
    context: services/marimo
  restart: unless-stopped
  expose:
    - 8080
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
reverse_proxy marimo:8080
```
