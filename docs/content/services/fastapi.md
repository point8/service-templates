# FastAPI

Website: [fastapi.tiangolo.com/](https://fastapi.tiangolo.com/)

Everything is located in the `fastapi/` directory. Feel free to add your own code. A basic app can be found in `fastapi/backend/main.py`.

To visit the API documentation append `/docs` to the URL., e.g. [https://localhost/docs](https://localhost/docs).

## Dockerfile

To change the command running the app, you need to adapt the last line in the `Dockerfile` to reflect those changes:

```
CMD ["poetry", "run", "uvicorn", "example:app", "--host", "0.0.0.0", "--port", "8080"]
```

## docker-compose

Add the following configuration block as a service to the `compose.yaml` file:

```yaml
fastapi:
  build:
    context: services/fastapi
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
reverse_proxy fastapi:8080
```
