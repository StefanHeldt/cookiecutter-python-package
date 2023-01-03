### Builder ###
FROM python:3.10-slim AS builder

ENV APP_HOME=/home/app \
    VENV=/home/app/.venv \
    PIP_DEFAULT_TIMEOUT=100 \
    PIP_DISABLE_PIP_VERSION_CHECK=1 \
    PIP_NO_CACHE_DIR=1 \
    PYTHONUNBUFFERED=1 \
    PYTHONDONTWRITEBYTECODE=1 \
    PYTHONFAULTHANDLER=1 \
    POETRY_NO_INTERACTION=1 \
    POETRY_VIRTUALENVS_CREATE=false

RUN python3 -m venv ${VENV} \
    && ${VENV}/bin/pip install --upgrade pip poetry==1.2.2 poetry-core==1.4.0 \
    && ${VENV}/bin/poetry config virtualenvs.create false

COPY . ${APP_HOME}
WORKDIR ${APP_HOME}
RUN ${VENV}/bin/poetry install -v --no-dev --no-ansi

### Tester ###
FROM builder AS tester
RUN ${VENV}/bin/pip install pytest pytest-cov && ${VENV}/bin/pytest

# ### Final ###
FROM python:3.10-slim
LABEL maintainer="{{cookiecutter.author}}"

ENV APP_HOME=/home/app \
    VENV=/home/app/.venv \
    PYTHONUNBUFFERED=1 \
    PYTHONDONTWRITEBYTECODE=1 \
    PYTHONFAULTHANDLER=1

COPY --from=builder ${VENV} ${VENV}

ENV PATH="${VENV}/bin:${PATH}"

COPY . ${APP_HOME}
WORKDIR ${APP_HOME}

ENTRYPOINT [ "{{cookiecutter.project_name}}" ]
