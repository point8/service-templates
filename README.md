# streamlit-standalone-template

## Run your own TLS secured service in not that many easy steps:

1. Open a [new Issue](https://git.point-8.de/it/tachyon/-/issues/new) and request the `<subdomain>.point8.cloud` you need and if you have any requirements on the computational part (If not, you get a [CPX11](https://www.hetzner.com/de/cloud)). Assign the Issue to Christophe. Then wait for the issue to be resolved.

1. In the meantime, change the domain in the `CNAME` file to your requested Subdomain.

1. Also decide on the service you want to deploy and change the name in the `SERVICE` file respectively.

1. Add a host entry to your `~/.ssh/config`

1. As soon as the issue is done, run `make init`

1. To deploy run `make deploy`


### Change basic authentication

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
