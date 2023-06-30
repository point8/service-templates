# Streamlit

Website: [streamlit.io/](https://streamlit.io/)

Everything is located in the `streamlit/` directory. Feel free to add your own code. A basic app can be found in `streamlit/app.py`.

## Dockerfile

To change the command running the app, you need to adapt the last line in the `Dockerfile` to reflect those changes:

```
CMD ["poetry", "run", "streamlit", "run", "app.py"]
```

## docker-compose

Add the following configuration block as a service to the `compose.yaml` file:

```yaml
streamlit:
  build:
    context: ./streamlit
  restart: unless-stopped
  expose:
    - 8501
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
reverse_proxy streamlit:8501
```
