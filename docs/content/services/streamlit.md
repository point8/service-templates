# Streamlit

Everything is located in the `streamlit/` directory. Feel free to add your own code. A basic app can be found in `streamlit/app.py`.

## Dockerfile

If you somehow need to change the command the streamlit app is run, you need to adapt the last line in the `Dockerfile` to reflect those changes:

```
CMD ["poetry", "run", "streamlit", "run", "app.py"]
```

## docker-compose

Add the following configuration block as a service in the `compose.yaml` file:

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

To redirect all external HTTPs requests to the streamlit service change the revers proxy line in the `Caddyfile` to:

```Caddyfile
reverse_proxy streamlit:8501
```
