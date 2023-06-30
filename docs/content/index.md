# Welcome

![logo.png](i/logo.png)

_(Public mirror: https://github.com/point8/service-templates)_

## Run your own TLS secured data (visualization) service with docker

Running your [streamlit](https://streamlit.io/), [voila](https://voila.readthedocs.io/en/stable/index.html), [dash](https://dash.plotly.com/) or [FastAPI](https://fastapi.tiangolo.com) app as a cloud service with a simple password authentication and secured by HTTPS.

The repository consists of example apps and a reverse proxy to automatically handle the HTTPS endpoint and TLS certificates. Everything is glued together and deployed using [`docker-compose`](https://docs.docker.com/compose/).

Additionally NoSQL and SQL database services are available and a Redis service is configured to if one is needed. See the [Auxiliary services](auxiliary-services.md) page.

The service gets automatically deployed using [`ansible`](https://docs.ansible.com/ansible/latest/index.html) from inside the GitLab CI.

### How to start?

Fork the repo and then go through the following parts one by one. Please read through the whole documentation once before touching anything.

There are different service templates available:

- [streamlit](services/streamlit.md)
- [FastAPI](services/fastapi.md)
- [voila](services/voila.md)
- [dash](services/dash.md)

Feel free to add more by opening a MR.

After you decided what kind of service you want to use, you have to adapt your file in two places:

1. Update the `compose.yaml` and also review all dependencies (`depends_on:`, `volumes:`)
2. Pick the correct `reverse_proxy` in the `Caddyfile`

Make sure to update your dependencies and keep the `pyproject.toml` and the `poetry.lock` files up to date. Also make sure, that the Python version dependency is the same as set in `.python-version`.

Also check if you need or want to pin the image tags of the services to a specific version.

### Development

You can develop everything local

* Spin everything up using (in the repository root, not inside the service template directory!)
    ```
    docker-compose up --build
    ```
* If you make changes repeat the last step.
* Visit your page under [https://localhost](https://localhost) (You have override the browser warnings, see "Reverse Proxy and TLS").

#### Python

Python is handeled by [`pyenv`](). The version is fixed in the `.python-version` file by calling `pyenv local X.Y.Z`.
