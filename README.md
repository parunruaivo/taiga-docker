## Prerequisites

* [Docker](https://docs.docker.com/engine/installation/)
* [Docker Compose](https://github.com/docker/compose/releases/tag/1.8.0)

## Quick start

1. Clone the repository and move to the directory
    ```shell
    git clone https://github.com/parunruaivo/taiga-docker.git
    cd taiga-docker
    ```

2. Start the containers
    ```shell
    docker-compose up -d
    ```
    
3. Access to taiga with the url **http://taiga.127.0.0.1.xip.io**

## Configuration parameters

| Parameter             | Description               |
|---                    |---                        |
| `DEBUG`                 | Set this to `true` to enable taiga debug mode. Defaults to `false`.                          |
| `TEMPLATE_DEBUG`                 | Defaults to `false`                          |
| `DB_HOST`                 | The database server hostname. Defaults to `localhost`                          |
| `DB_PORT`                 | The database server port. Defaults to `5432`                          |
| `DB_USER`                 | The database database user. Defaults to `postgres`                          |
| `DB_PASS`                 | The database database password. Defaults to `postgres`                          |
| `DB_NAME`                 | The database database name. Defaults to `postgres`                          |
| `TAIGA_HOST`                 | The hostname of the Taiga server. Defaults to `localhost`                          |
| `TAIGA_ROOT_USERNAME`                 | The password for the root user on firstrun. Defaults to `admin`                          |
| `TAIGA_ROOT_EMAIL`                 | The email for the root user on firstrun. Defaults to `admin@admin.com`                         |
| `TAIGA_HTTPS`                 | Defaults to `false`                          |
| `TAIGA_SECRET_KEY`                 | Defaults to `secretkey`                          |
| `PUBLIC_REGISTER_ENABLED`                 | Defaults to `true`                          |
| `WEBHOOKS_ENABLED`                 | Defaults to `false`                          |
| `STATS_ENABLED`                 | Defaults to `false`                          |
| `FRONT_SITEMAP_CACHE_TIMEOUT`                 | Defaults to `360`                          |
| `FRONT_SITEMAP_ENABLED`                | Defaults to `false`                          |
| `FRONT_SITEMAP_CACHE_TIMEOUT`                 | Defaults to `8640`                          |
| `EMAIL_ENABLED`                 | Defaults to `false`                          |
| `EMAIL_HOST`                 | Defaults to `smtp.gmail.com`                          |
| `EMAIL_PORT`                 | Defaults to `587`                          |
| `EMAIL_USER`                 | Defaults to `example@gmail.com`                          |
| `EMAIL_PASS`                 | Defaults to `secret`                          |
| `EMAIL_USE_TLS`                 | Defaults to `true`                          |
| `TAIGA_EMAIL`                 | Defaults to `notifications@example.com`                          |
| `DEFAULT_FROM_EMAIL`                 | Defaults to `noreply@example.com`                          |
| `CELERY_ENABLED`                 | Defaults to `false`                          |
| `CELERY_AMQP_NAME`                 | Defaults to `/`                          |
| `EVENTS_ENABLED`                 | Defaults to `false`                          |
| `EVENTS_AMQP_NAME`                 | Defaults to `taiga`                          |
| `AMQP_HOST`                 | Defaults to `localhost`                          |
| `AMQP_PORT`                 | Defaults to `5672`                          |
| `AMQP_USER`                 | Defaults to `guest`                          |
| `AMQP_PASS`                 | Defaults to `guest`                          |
| `REDIS_HOST`                 | Defaults to `localhost`                          |
| `REDIS_PORT`                 | Defaults to `6379`                          |
| `REDIS_DB_NUMBER`                 | Defaults to `0`                          |
| `GITHUB_ENABLED`                 | Defaults to `false`                          |
| `GITHUB_URL`                 | Defaults to `https://github.com/`                          |
| `GITHUB_API_URL`                 | Defaults to `https://api.github.com/`                          |
| `GITHUB_API_CLIENT_ID`                 | Defaults to `yourgithubclientid`                          |
| `GITHUB_API_CLIENT_SECRET`                 | Defaults to `yourgithubclientsecret`                          |
| `FEEDBACK_ENABLED`                 | Defaults to `false`                          |
| `FEEDBACK_EMAIL`                 | Defaults to `support@taiga.io`                          |
