# RestAPI Test Task

## Запуск приложения:

1. Склонируйте репозиторий и перейдите в корень проекта:
    ```shell
    git clone <URL_репозитория>
    cd <название_проекта>
    ```
2. Создайте `.env` файл в корне проекта (пример см. `.env.example`):
    ```shell
    cp .env.example .env
    ```
3. Поднимите контейнеры Docker:
    ```shell
    docker compose up
    ```
4. Примените миграции Alembic:
    ```shell
    alembic upgrade head
    ```
