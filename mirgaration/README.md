Generic single-database configuration.


Алгоритм создания alembic и миграций между версиями
- Создаем директорию alembic
`alembic init alembic`
- В файле alembic.ini настрайваем переменную sqlalchemy.url под свою базу
- Создаем таблицу alembic_version_history через файл create_alembic_version_history.sql (описание настройки взято [тут](https://stackoverflow.com/questions/73248731/alembic-store-extra-information-in-alembic-version-table))
- Создаем новую ревизию
`alembic revision -m "your description"`
- Заполняем там нужные измения, но если была команда (`alembic revision --autogenerate -m "your description"`) заполнять ничего не нужно
- Делаем апгрейд ревизии
`alembic upgrade head`

Туториал https://alembic.sqlalchemy.org/en/latest/tutorial.html
