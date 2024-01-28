# stocks_assistant
Проект-бэкенд для тренажёра трейдера

Миграция alembic [here](./alembic/README.md)

Docker [конструкции](https://tproger.ru/translations/docker-instuction/), [гайд](https://habr.com/ru/post/310460/)
Переченные среды устанавливаем через файл env.list

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


### Poetry
1. `brew install poetry`
2. `poetry install`
3. `poetry shell` - если ещё нет окружения
4. `poetry env info` - проверка в каком окружении сейчас
5. в окружении запускаем сервак `uvicorn main:app --reload`
