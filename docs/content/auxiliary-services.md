### Auxiliary services

#### PostgreSQL

An instance of [PostgreSQL](https://www.postgresql.org/) is available. Please check the preconfigured environment variables under `environment:` if they need to be adapted.

It uses the standard port `5432` and can be accessed internally by all other services e.g. via string `postgresql://<username>:<password>@postgres:5432`

For further documentation please see the [official documentation](https://hub.docker.com/_/postgres) of the docker image.

Add, replace, or update the following block in the `compose.yaml` to use this service (and check all `depends_on` lists):

```yaml
postgres:
  image: postgres:latest
  restart: unless-stopped
  expose:
    - 5432
  environment:
    - POSTGRES_USER=postgres
    - POSTGRES_PASSWORD=pf9K6bCTkz2rgCzgN2AsWLRuK8
    - POSTGRES_DB=example
  volumes:
    - postgres-data:/var/lib/postgresql/data
  networks:
    - local
```

Feel free to set other environment variables.

#### MongoDB

An instance of [MongoDB](https://www.mongodb.com/) is available. Please check the preconfigured environment variables under `environment:` if they need to be adapted.

It uses the standard port `27017` and can be accessed internally by all other services e.g. via string `mongodb://<username>:<password>@mongodb:27017`

For further documentation please see the [official documentation](https://hub.docker.com/_/mongo) of the docker image.

Add, replace, or update the following block in the `compose.yaml` to use this service

```yaml
mongodb:
  image: mongo:latest
  volumes:
    - mongodb-data:/data/db
  environment:
    - MONGO_INITDB_ROOT_USERNAME=mongodb
    - MONGO_INITDB_ROOT_PASSWORD=n2mYJ9BhU2AaVnrNZVzNJt4hsC
    - MONGO_INITDB_DATABASE=example
  networks:
    - local
```

Feel free to set other environment variables.

#### Redis

An instance of [Redis](https://redis.io/) is available. Please check the preconfigured environment variables under `environment:` if they need to be adapted.

It uses the standard port `6379` and can be accessed internally by all other services e.g. via string `redis://redis:6379/0`

For further documentation please see the [official documentation](https://hub.docker.com/_/redis) of the docker image.

Add, replace, or update the following block in the `compose.yaml` to use this service

```yaml
redis:
  image: redis:latest
  restart: unless-stopped
  expose:
   - 6379
  volumes:
    - redis-data:/data
  networks:
    - local
```
