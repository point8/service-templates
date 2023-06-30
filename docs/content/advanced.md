# Advanced setups

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
