# streamlit-standalone-template

## Getting started

Run `make init` then `docker-compose up`

### Change basic authentication

The authentication to the service is done using HTTP basic auth.

The default credentials are `guest:geheim`

See the following section in the `Caddyfile`

```
basicauth {
    guest JDJhJDE0JEhDc0lEcGRraS94SFZ1TzlEUjl5Wi5WM3hOa0xWSlVQYzBOS0xJMmwzczN4Qk9zbnlUU29p
}
```

To create a new password use e.g.

```
docker run -it caddy caddy hash-password --plaintext 1-super-secret-pa$$word
```
