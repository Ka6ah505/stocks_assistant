# base image
FROM python:3.11.3-slim
# мета данные контейнера
LABEL mainteiner="ka6ah505@gmail.com"
# переменные окружений
ENV PYTHONUNBUFFERED 1
# открытие портов
EXPOSE 8000
#EXPOSE 5432
# Установка рабочей директории
WORKDIR /app
# копирование файлов
COPY . /app
# Запуск команд
RUN pip install poetry
RUN apt-get update \
    && apt-get install -y postgresql-server-dev-all gcc python3-dev musl-dev
RUN poetry install --without dev
CMD ["poetry", "run", "uvicorn", "--host", "0.0.0.0", "main:app", "--proxy-headers"]
#RUN pip install --no-cache-dir --upgrade -r /app/requirements.txt
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