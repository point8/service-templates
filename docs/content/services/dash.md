# Dash

Website: [dash.plotly.com/](https://dash.plotly.com/)

Everything is located in the `dash/` directory. Feel free to add your own code. A basic app can be found in `dash/example.py`.

## Dockerfile

To change the command running the app, you need to adapt the last line in the `Dockerfile` to reflect those changes:

```
CMD ["poetry", "run", "gunicorn", "example:server", "-b", ":8050"]
```

## docker-compose

Add the following configuration block as a service to the `compose.yaml` file:

```yaml
dash:
  build:
    context: services/dash
  restart: unless-stopped
  expose:
    - 8050
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
reverse_proxy dash:8050
```
