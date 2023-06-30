# Authentication

## Change basic authentication

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
