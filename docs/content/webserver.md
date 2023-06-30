# Webserver

Requests to the service are handled by [Caddy 2](https://caddyserver.com/), a modern web server and reverse proxy that also automatically handles HTTPS and certificates.

### Reverse Proxy and TLS

Everything is configured in the `Caddyfile`.

* If you want to test locally, replace the URL (`service-templates.point8.cloud`) in line 4 in the `Caddyfile` with `localhost`.

As long as you test it locally you have to accept/override your browser warnings caused by an "insecure" TLS connection due to an untrusted self-signed certificate.

### Security

Besides TLS, Caddy also handles authentication, see the [Authentication page](auth.md) for further help.
