FROM python:3-slim

WORKDIR /tmp/app
RUN pip install poetry

COPY ./pyproject.toml .
RUN poetry install

COPY . .

ENTRYPOINT poetry run python hello_python/app.py