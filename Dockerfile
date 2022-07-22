# base image
FROM python:3.9-slim
# мета данные контейнера
LABEL mainteiner="ka6ah505@gmail.com"
# переменные окружений
ENV PYTHONUNBUFFERED 1
ENV DATABASE yeyhwxzv
ENV PORT 5432
ENV HOST castor.db.elephantsql.com
ENV PASSWORD OYGqbbGxYHlFuwRUVVgroP6vLV9_89bI
# открытие портов
EXPOSE 8000
EXPOSE 5432
# Установка рабочей директории
WORKDIR /app
# копирование файлов
COPY . /app
# Запуск команд
RUN apt-get update \
    && apt-get install -y postgresql-server-dev-all gcc python3-dev musl-dev
RUN pip install --no-cache-dir --upgrade -r /app/requirements.txt
## копирует + может распаковать .tar
#ADD
# Запуск команда и аргументы для выполнения внутри контейнера. Только одна конструкция
#CMD ['python3', '-m', 'uvicorn', 'main:app', '--reload', '--host=0.0.0.0']

## Переменная для передачи в докер во время сборки
#ARG
## Команды для выполняющегося контейнера
#ENTRYPOINT
## точка подключения к дериктории и место хранения статических файлов
#VOLUME