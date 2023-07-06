# Advanced setups

## Devcontainers

An example [devcontainer](https://containers.dev) setup is provided under `.devcontainer`.

It consists of a backend services, a reverse proxy and a frontend app. The `devcontainer` in this setup can be used to develop the [svelte](https://svelte.dev) frontend, while the [FastAPI](https://fastapi.tiangolo.com) example provides a backend.

Everything is defined in the `.devcontainer` directory. The central part of the setup is the `devcontainer.json`, there a [docker-compose](https://docs.docker.com/compose/) based environment is defined. The `compose.yaml` describes the different services used, where `frontend` is the service we will connect to, in order to develop the frontend.

The source code of the backend service is also mounted to the backend container, thus allowing the backend server to refresh as the code is updated.

### Using VSCode and the devcontainer extension

There are other ways you can work with devcontainer, but here we will use the VSCode extension: [Dev Containers](https://marketplace.visualstudio.com/items?itemName=ms-vscode-remote.remote-containers).

Please follow to the instructions to set the extension up and install docker locally.

Then you can open the VSCode Command Palette and type `Dev Containers`, choose `Reopen in Container` and wait for the several docker containers to spin up.

You can use the terminal in VSCode to execute commands inside the devcontainer. As we are using a [nodejs](https://nodejs.org) image, we can start the svelte dev server with

```
cd services/svelte
npm install
npm run dev
```

You can then visit the results in your browser, VSCode will provide the tunnel automatically.

If you are done, you can use the Command Palette again and run `Reopen in local folder` to exit the devcontainer.

Further [documentation](https://code.visualstudio.com/docs/remote/remote-overview) is available online.

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
