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
5. При необходимости наполните базу данных тестовыми данными. При использовании переменных, указанных в `.env.example`, получится команда:
   ```shell
   psql postgresql://postgres:postgres@localhost:5433/postgres -f infra/infra.sql
   ```
6. Для доступа к Swagger перейдите по ссылке, которая, при использовании переменных, указанных в `.env.example`, выглядит так:
   ```shell
   http://0.0.0.0:8000/docs
   ```