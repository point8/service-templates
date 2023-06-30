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
