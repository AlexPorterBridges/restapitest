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
5. При необходимости наполните базу данных тестовыми данными. Подставьте необходимые параметры из `.env` в команду ниже:
   ```shell
   psql postgresql://{login}:{password}@{host_external}:{port_external}/{name} -f infra/infra.sql
   ```
   так, при использовании переменных, указанных в `.env.example`, получится команда:
   ```shell
   psql postgresql://postgres:postgres@localhost:5433/postgres -f infra/infra.sql
   ```