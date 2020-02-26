FROM python:3-slim

ENV PYTHONUNBUFFERED 1
ENV PYTHONDONTWRITEBYTECODE 1

WORKDIR /tmp/app
RUN pip install poetry

COPY ./pyproject.toml .
RUN poetry install

COPY . .

ENTRYPOINT poetry run python hello_python/app.py