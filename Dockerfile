FROM python:3.11-slim

RUN apt-get update && apt-get install -y curl \
    && curl -sSL https://install.python-poetry.org | python3 - \
    && apt-get clean

ENV PATH="/root/.local/bin:$PATH"

COPY pyproject.toml poetry.lock ./
RUN poetry install --no-root --no-dev && poetry cache clear --all pypi

COPY .env .env
COPY apis/shared.py .