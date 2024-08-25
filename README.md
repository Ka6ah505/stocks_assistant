# stocks_assistant
&nbsp;

![GitHub Issues or Pull Requests](https://img.shields.io/github/issues-pr/ka6ah505/stocks_assistant)
![GitHub Issues or Pull Requests](https://img.shields.io/github/issues-pr-closed/ka6ah505/stocks_assistant)
![GitHub commit activity](https://img.shields.io/github/commit-activity/t/ka6ah505/stocks_assistant)

Проект-бэкенд для тренажёра трейдера

Миграция alembic [here](./migration/README.md)

Docker [конструкции](https://tproger.ru/translations/docker-instuction/), [гайд](https://habr.com/ru/post/310460/)
Переченные среды устанавливаем через файл env.list

### Endpoints:
1. `GET /`
2. `GET /api/v1/info` - Получаем информацию о системе/сервере
3. `GET /api/v1/all` - Получаем все записи из таблицы `stock_price`
4. `GET /api/v1/stocks/{self}` - Получаем запись по конкретному тикету из таблицы `stock_price`
5. `POST /api/v1/stocks` - добавление стоимости бумаги
```josn 
[
  {
    "ticket": "string",
    "datetime": "2024-08-25T09:28:02.970Z",
    "open": 0,
    "high": 0,
    "low": 0,
    "close": 0,
    "volume": 0,
    "timeframe": "string"
  }
]
```

### Database schema
Схема создана в [dbdiagram.io](https://dbdiagram.io) [сама схема](https://dbdiagram.io/embed/624953fed043196e39e57b34)


### Poetry
1. `brew install poetry`
2. `poetry install`
3. `poetry shell` - если ещё нет окружения
4. `poetry env info` - проверка в каком окружении сейчас
5. в окружении запускаем сервак `uvicorn main:app --reload`

![Static Badge](https://img.shields.io/badge/python-3.11-74aa9c?style=for-the-badge&logo=python)
![Static_Badge](https://img.shields.io/badge/fastApi-74aa9c?style=for-the-badge&logo=fastapi)
![Static_Badge](https://img.shields.io/badge/alembic-74aa9c?style=for-the-badge&logo=alembic)
![Static_Badge](https://img.shields.io/badge/sqlalchemy-74aa9c?style=for-the-badge&logo=sqlalchemy)
![Static_Badge](https://img.shields.io/badge/redis-%23DD0031.svg?&style=for-the-badge&logo=redis&logoColor=white)
![Static_Badge](https://img.shields.io/badge/GitHub-100000?style=for-the-badge&logo=github&logoColor=white)
![Static_Badge](https://img.shields.io/badge/PostgreSQL-316192?style=for-the-badge&logo=postgresql&logoColor=white)
![Static_Badge](https://img.shields.io/badge/PyCharm-000000.svg?&style=for-the-badge&logo=PyCharm&logoColor=white)
![Static_Badge](https://img.shields.io/badge/iTerm2-000000?style=for-the-badge&logo=iterm2&logoColor=white)

![Static_Badge](https://github-readme-stats.vercel.app/api/top-langs/?username=Ka6ah505&theme=blue-green)
![Static_Badge](https://github-readme-stats.vercel.app/api?username=ka6ah505&theme=blue-green)