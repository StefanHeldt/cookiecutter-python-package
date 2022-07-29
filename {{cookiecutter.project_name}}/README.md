# {{ cookiecutter.friendly_name }}


[![Tests](https://github.com/{{cookiecutter.github_user}}/{{cookiecutter.project_name}}/workflows/Tests/badge.svg)][tests]
[![pre-commit](https://img.shields.io/badge/pre--commit-enabled-brightgreen?logo=pre-commit&logoColor=white)][pre-commit]
[![Black](https://img.shields.io/badge/code%20style-black-000000.svg)][black]

[tests]: https://github.com/{{cookiecutter.github_user}}/{{cookiecutter.project_name}}/actions?workflow=Tests
[pre-commit]: https://github.com/pre-commit/pre-commit
[black]: https://github.com/psf/black

{{cookiecutter.project_short_description}}

## Features

- TODO

## Requirements
Python 3.10 and [poetry](https://python-poetry.org). 

## Installation
If you don't have poetry, install it using
```console
curl -sSL https://install.python-poetry.org/install-poetry.py | python -
```
Configure poetry to not create virtualenvs and use in-project virtualenvs
```console
poetry config virtualenvs.create false
poetry config virtualenvs.create true
```

To set up a development environment run `make dev` in a terminal. This should:
- Create a virtual environment with Python 3.10
- Activate the virtual environment and install `poetry`
- Install the dependencies described in `pyproject.toml` file
- Install the pre-commit hooks

Activate your development environment with
```console
source .venv/bin/activate
```

## Usage
Once installed, you can run the package via its command line entry point
```console
{{cookiecutter.project_name}}
```

## Issues

- TODO
