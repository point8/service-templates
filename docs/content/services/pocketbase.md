# PocketBase

Website: [pocketbase.io/](https://pocketbase.io/)

Everything is located in the `pocketbase/` directory.

## Dockerfile

To change the command running the app, you need to adapt the last line in the `Dockerfile` to reflect those changes:

```
CMD ["/pb/pocketbase", "serve", "--http=0.0.0.0:8008"]
```

## docker-compose

Add the following configuration block as a service to the `compose.yaml` file:

```yaml
  pocketbase:
    build:
      context: services/pocketbase
    restart: unless-stopped
    expose:
      - 8008
    # uncomment for local access under http://localhost:8008/_/
    # ports:
    #   - "8008:8008"
    volumes:
      - pocketbase-data:/pb/pb_data
    networks:
      - local
```

And declare the docker volume at the end of the compose file

```
volumes:
  ...
  pocketbase-data:
```

### Access the admin portal through tailscale

If you want to access the admin portal you need to make it accessible to the host. To do so, please uncomment the port forwarding as stated above.

Then you can access the portal securely through tailscale:

```
sudo ufw route allow in on tailscale0 from any to any port 8008 proto tcp comment "TMP grant access to local pocketbase container"
```

After that the site can be reached via: `http://hostname.neon-tuna.ts.net:8008/_/`

## Caddyfile

To redirect HTTPs requests to the service add a `handle_path` directive with a `reverse_proxy` line to the `Caddyfile`:

```
    handle_path /pb/* {
        reverse_proxy pocketbase:8008 
    }
```

This will then create a relative path you can use from your frontend, i.e.:

```js
import PocketBase from 'pocketbase';

const pb = new PocketBase('/pb/');
```
