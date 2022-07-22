Generic single-database configuration.


Алгоритм создания alembic и миграций между версиями
- Создаем директорию alembic
`alembic init alembic`
- Добавляем в .gitignore файл alembic.ini
- В файле alembic.ini настрайваем переменную sqlalchemy.url под свою базу
- Создаем новую ревизию
`alembic revision -m "your description"`
- Заполняем там нужные измения
- Делаем апгрейд ревизии
`alembic upgrade head`

Туториал https://alembic.sqlalchemy.org/en/latest/tutorial.html

Добавил ветку для разработки "dev"
