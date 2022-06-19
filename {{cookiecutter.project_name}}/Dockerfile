### Builder ###
FROM python:3.10.1-slim-buster AS builder

ENV APP_HOME=/home/app \
    VENV=/home/app/.venv \
    PIP_DEFAULT_TIMEOUT=100 \
    PIP_DISABLE_PIP_VERSION_CHECK=1 \
    PIP_NO_CACHE_DIR=1

RUN python3 -m venv ${VENV} \
    && ${VENV}/bin/pip install --upgrade pip poetry==1.1.13 poetry-core==1.0.7 \
    && ${VENV}/bin/poetry config virtualenvs.create false

### Virtual Environment ###
FROM builder AS builder-venv

ENV APP_HOME=/home/app \
    VENV=/home/app/.venv \
    PIP_DEFAULT_TIMEOUT=100 \
    PIP_DISABLE_PIP_VERSION_CHECK=1 \
    PIP_NO_CACHE_DIR=1 \
    PYTHONUNBUFFERED=1 \
    PYTHONDONTWRITEBYTECODE=1 \
    PYTHONFAULTHANDLER=1 \
    \
    POETRY_NO_INTERACTION=1 \
    POETRY_VIRTUALENVS_CREATE=false

COPY poetry.lock pyproject.toml ${APP_HOME}
WORKDIR ${APP_HOME}
RUN ${VENV}/bin/poetry install -v --no-dev --no-ansi

### Tester ###
# FROM builder-venv AS tester

# COPY . ${APP_HOME}
# RUN ${VENV}/bin/pip install pytest pytest-cov && ${VENV}/bin/pytest

### Final ###
FROM python:3.10.1-slim-buster
LABEL maintainer="{{cookiecutter.author}}"

ENV APP_HOME=/home/app \
    VENV=/home/app/.venv \
    PYTHONUNBUFFERED=1 \
    PYTHONDONTWRITEBYTECODE=1 \
    PYTHONFAULTHANDLER=1 \
    POETRY_NO_INTERACTION=1 \
    POETRY_VIRTUALENVS_CREATE=false

COPY --from=builder-venv ${VENV} ${VENV}

COPY . ${APP_HOME}
WORKDIR ${APP_HOME}

CMD {{cookiecutter.project_name}}
