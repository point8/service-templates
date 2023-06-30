# How to start?

![logo.png](i/logo.png)

_(Public mirror: https://github.com/point8/service-templates)_

## Run your own TLS secured data (visualization) service with docker

Running your [streamlit](https://streamlit.io/), [voila](https://voila.readthedocs.io/en/stable/index.html), [dash](https://dash.plotly.com/) or [FastAPI](https://fastapi.tiangolo.com) app as a cloud service with a simple password authentication and secured by HTTPS.

The repository consists of example apps and a reverse proxy to automatically handle the HTTPS endpoint and TLS certificates. Everything is glued together and deployed using [`docker-compose`](https://docs.docker.com/compose/).

Additionally NoSQL and SQL database services are available and a Redis service is configured to if one is needed.

The service gets automatically deployed using [`ansible`](https://docs.ansible.com/ansible/latest/index.html) from inside the GitLab CI.

## How to start?

Fork the repo and then go through the following parts one by one. Please read through the whole README once before touching anything.

At the moment

- streamlit
- voila
- dash
- FastAPI

templates are included. Feel free to add another one by opening a MR.

### Python

Python is handeled by [`pyenv`](). The version is fixed in the `.python-version` file by calling `pyenv local X.Y.Z`.

### Services

There are different service templates available. See below.

After you decided what kind of service you want to use, you have to adapt your file in two places:

1. Remove all unused services from the `compose.yaml` and also remove all unused dependencies (`depends_on:`, `volumes:`)
2. Pick the correct `reverse_proxy` in the `Caddyfile`

Make sure to update your dependencies and keep the `pyproject.toml` and the `poetry.lock` files up to date. Also make sure, that the Python version dependency is the same as set in `.python-version`.

Also check if you need or want to pin the image tags of the services to a specific version.

#### Streamlit

Everything is located in the `streamlit/` directory. Feel free to add your own code. A basic app can be found in `streamlit/app.py`.

If you somehow need to change the command the streamlit app is run, you need to adapt the last line in the `Dockerfile` to reflect those changes:

```
CMD ["poetry", "run", "streamlit", "run", "app.py"]
```

#### Voilà

Everything is located in the `voila/` directory. Feel free to add your own code. A basic app can be found in `voila/example.ipynb`.

If you somehow need to change the command the voila app is run, you need to adapt the last line in the `Dockerfile` to reflect those changes:

```
CMD ["poetry", "run", "voila", "--no-browser", "--Voila.ip='0.0.0.0'", "--port=8866", "example.ipynb"]
```

If you remove the last part (`"example.ipynb"`), the user gets a list of all available notebooks.

#### Dash

Everything is located in the `dash/` directory. Feel free to add your own code. A basic app can be found in `dash/example.py`.

If you somehow need to change the command the dash app is run, you need to adapt the last line in the `Dockerfile` to reflect those changes:

```
CMD ["poetry", "run", "gunicorn", "example:server", "-b", ":8050"]
```

#### FastAPI

Everything is located in the `fastapi/` directory. Feel free to add your own code. A basic app can be found in `fastapi/example.py`.

If you somehow need to change the command the FastAPI app is run, you need to adapt the last line in the `Dockerfile` to reflect those changes:

```
CMD ["poetry", "run", "uvicorn", "example:app", "--host", "0.0.0.0", "--port", "8080"]
```

To visit the API documentation append `/docs` to the URL., e.g. [https://localhost/docs](https://localhost/docs).

### Auxiliary services

#### PostgreSQL

An instance of [PostgreSQL](https://www.postgresql.org/) is available. Please check the preconfigured environment variables under `environment:` if they need to be adapted.

It uses the standard port `5432` and can be accessed internally by all other services e.g. via string `postgresql://<username>:<password>@postgres:5432`

For further documentation please see the [official documentation](https://hub.docker.com/_/postgres) of the docker image.

#### MongoDB

An instance of [MongoDB](https://www.mongodb.com/) is available. Please check the preconfigured environment variables under `environment:` if they need to be adapted.

It uses the standard port `27017` and can be accessed internally by all other services e.g. via string `mongodb://<username>:<password>@mongodb:27017`

For further documentation please see the [official documentation](https://hub.docker.com/_/mongo) of the docker image.

#### Redis

An instance of [Redis](https://redis.io/) is available. Please check the preconfigured environment variables under `environment:` if they need to be adapted.

It uses the standard port `6379` and can be accessed internally by all other services e.g. via string `redis://redis:6379/0`

For further documentation please see the [official documentation](https://hub.docker.com/_/redis) of the docker image.

### Reverse Proxy and TLS

[Caddy](https://caddyserver.com/) is used to act as a reverse proxy, handle TLS certificates, and forward the user from the standard HTTP(s) ports to your hidden service in the background.

Everything is configured in the `Caddyfile`.

* If you want to test locally, replace the URL (`service-templates.point8.cloud`) in line 4 in the `Caddyfile` with `localhost`.

As long as you test it locally you have to accept/override your browser warnings caused by an "insecure" TLS connection due to an untrusted self-signed certificate.

#### Change basic authentication

The authentication to the service is done using HTTP basic auth.

The default credentials are `guest:geheim`

The following section in the `Caddyfile` is responsible for setting it.

```
basicauth {
    guest JDJhJDE0JEhDc0lEcGRraS94SFZ1TzlEUjl5Wi5WM3hOa0xWSlVQYzBOS0xJMmwzczN4Qk9zbnlUU29p
}
```

To create a new password use e.g.

```
docker run -it caddy:latest caddy hash-password --plaintext "1-super-secret-pa$$word"
```

If you omit the `--plaintext` option, you can type in the password interactively.

Feel free to adapt the set credentials to your needs. Remember to update the username and password hash in the `Caddyfile` after you generated new credentials.

### Development

You can develop everything local

* Create the internal and external docker networks
    ```
    docker network create web
    docker network create --internal local
    ```
* Spin everything up using (in the repository root, not inside the service template directory!)
    ```
    docker-compose up --build
    ```
* If you make changes repeat the last step.
* Visit your page under [https://localhost](https://localhost) (You have override the browser warnings, see "Reverse Proxy and TLS").

## Launch multiple applications at subdomains
It is possible to launch multiple apps and make them accessible at a self defined path. For better readability example names beginning with `my_` are used. These can be replaced by custom names.
1. Duplicate the service directory (streamlit/, fastapi/, ...) and rename it to `my_new_service_directiory`. Add the content of your additional application as described in the service section above.
2. Inside `compose.yaml` create another service:
    - Duplicate the section of the chosen service and rename it e.g. `streamlit` -> `my_new_service`.
    - Change the line `context: ./XXX` to the directory created in step 1 (`context: ./my_new_service_directiory`).
3. Add the following lines to the `Caddyfile` after the `reverse_proxy` statement:
    ```
    handle_path /your_custom_path/* {
        reverse_proxy my_new_service:XXXX 
    }
    ```
4. Deploy the service as described above. The new service is now reachable under `your_subdomain.point8.cloud/your_custom_path` as definde in the `Caddyfile`.

Currently this setup is only tested with streamlit applications, but should work with the other services too.
