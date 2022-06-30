# Service Templates

## Run your own TLS secured streamlit service with docker

Running your [streamlit](https://streamlit.io/) or [voila](https://voila.readthedocs.io/en/stable/index.html) app as a cloud service with a simple password authentication and secured by HTTPS.

The repository consists of a streamlit and voila app and a reverse proxy to automatically handle the HTTPS endpoint and TLS certificates. Everything is glued together and deployed using [`docker-compose`](https://docs.docker.com/compose/).

## How to start?

Fork the repo and then go through the following parts one by one.

At the moment only a streamlit and a voila app are included in the template. This can in principle be extended to other services.

### Server and Domain

* Open a [new Issue](https://git.point-8.de/it/tachyon/-/issues/new) and request the `<subdomain>.point8.cloud` you need and 
* if you have any requirements on the computational part (If not, you get a [CPX11](https://www.hetzner.com/de/cloud)).
* Also please specify how long the service will be needed.
* Who else besides you, needs administration access to the server?
* Assign the Issue to Christophe. Then wait for instructions. 

In the meantime you can continue with the next steps:


### SSH

You will connect to your new server using SSH. You can already add an entry to your `~/.ssh/config`:

```
Host your_subdomain.point8.cloud
    Hostname your_subdomain.point8.cloud
    User your_username
    Port 22122
    IdentityFile ~/.ssh/your_point8_ssh_key
    ForwardX11 yes
    ForwardAgent yes
```

### Python

Python is handeled by [`pyenv`](). The version is fixed in the `.python-version` file by calling `pyenv local X.Y.Z`.

### Service

There are different service templates available. See below.

After you decided what kind of service you want to use, you have to adapt your file in two places:

1. Remove all unused services from the `docker-compose.yml` and also remove the dependencies (`depends_on:`) under the `caddy:` service config.
2. Pick the correct `reverse_proxy` in the `Caddyfile`


#### Streamlit

Everything is located in the `streamlit/` directory. Feel free to add your own code. A basic app can be found in `streamlit/app.py`.

Make sure to update your dependencies and keep the `pyproject.toml` and the `poetry.lock` file up to date. Also make sure, that the Python version dependency is the same as set in `.python-version`.

If you somehow need to change the command the streamlit app is run, you need to adapt the last line in the `Dockerfile` to reflect those changes:

```
CMD ["poetry", "run", "streamlit", "run", "app.py"]
```

#### Voilà

Everything is located in the `voila/` directory. Feel free to add your own code. A basic app can be found in `voila/example.ipynb`.

Make sure to update your dependencies and keep the `pyproject.toml` and the `poetry.lock` file up to date. Also make sure, that the Python version dependency is the same as set in `.python-version`.

If you somehow need to change the command the voila app is run, you need to adapt the last line in the `Dockerfile` to reflect those changes:

```
CMD ["poetry", "run", "voila", "--no-browser", "--Voila.ip='0.0.0.0'", "--port=8866", "example.ipynb"]
```

If you remove the last part (`"example.ipynb"`), the user gets a list of all available notebooks.


### Reverse Proxy and TLS

[Caddy](https://caddyserver.com/) is used to act as a reverse proxy, handle TLS certificates, and forward the user from the standard HTTP(s) ports to your hidden service in the background.

Everything is configured in the `Caddyfile`.

* If you want to test everything locally, you can leave the `Caddyfile` as is, if you deploy it to a server you need to
* change the domain name in line 4 from `localhost` to `your_subdomain.point8.cloud`.

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
docker run -it caddy:latest caddy hash-password --plaintext 1-super-secret-pa$$word
```

Feel free to adapt the set credentials to your needs.

### Deployment

In order to deploy your service, you need to login into your server using SSH.

* Clone your repository
* Create the internal and external docker networks
    ```
    docker network create web
    docker network create --internal local
    ```
* Spin everything up using
    ```
    docker-compose up --build
    ```
* If you make changes, update the repository on the server and repead the last step.
