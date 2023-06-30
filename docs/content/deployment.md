# Deployment

In order to deploy your service, you need to login into your server using SSH.

* Clone your repository
* Create the internal and external docker networks
    ```
    docker network create web
    docker network create --internal local
    ```
* Spin everything up using
    ```
    docker-compose up --build
    ```
* If you make changes, update the repository on the server and repeat the last step.
* Use `docker-compose start/stop` to start and stop your service and `docker-compose down` to stop it and remove all containers
* If you are satisfied, you can run everything as a daemon with
    ```
    docker-compose up --detach
    ```
* Visit your page under the designated URL

## Automatic deployment using your projects CI pipeline

If you already have a server, than you can easily setup your project to be automatically deployed.

1. Ask Christophe or Vitorio to add the server SSH key to your projects CI variables.
2. Change the `TARGET_HOST` variable in the `.gitlab-ci.yml` file to your own `<subdomain>.point8.cloud` URL.
3. Done

All changes to the `main` branch are now deployed without further actions necessary.
