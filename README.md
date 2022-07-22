# stocks_assistant
Проект-бэкенд для тренажёра трейдера

Живёт на heroku где-то в тут https://stocks-assistant.herokuapp.com/api/v1/info

Миграция alembic [here](./alembic/README.md)

Docker [конструкции](https://tproger.ru/translations/docker-instuction/), [гайд](https://habr.com/ru/post/310460/)

### Endpoints:
1. `GET /`
2. `GET /api/v1/info` - Получаем информацию о системе/сервере
3. `GET /api/v1/all` - Получаем все записи из таблицы `Stock`
4. `GET /api/v1/prices/{ticket}` - Получаем запись по конкретному тикету из таблицы `Stock`
5. `POST /api/v1/add` - добавление стоимости бумаги
```josn 
body: {
    ticket: str
    close: float
}
```

### Database schema
Схема создана в [dbdiagram.io](https://dbdiagram.io) [сама схема](https://dbdiagram.io/embed/624953fed043196e39e57b34)
