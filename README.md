# Man Group Coding Test

![Python >= 3.10.2](https://img.shields.io/badge/python-%3E%3D%203.10.2-blue?style=flat-square) ![Testing Coverage 100%](https://img.shields.io/badge/coverage-100%25-green?style=flat-square)

## General Comments

* I have worked on this little project in my free time, around quite a busy work schedule.

* I have deliberately tried to focus on code readability, as opposed to optimisation ("premature optimisation is the root of all evil").

* My git commits are too large and infrequent, and my docstrings don't have much thought put into them. This is mainly to speed up development, in the knowledge that this is a toy app.

## Installation

I have chosen to use `poetry` and `pyenv`. To setup and use the environment:

```shell
poetry install
poetry shell
```

This will automatically create a virtual environment and install the required dependencies.

## Usage

```shell
python randomgen.py
```

The output will be as per `problem.pdf`.

## Development

### Pre-commit Checks

To run them manually:

```shell
pre-commit run --all-files
```

This will run a series of linting and type-checking (`flake8`, `black`, `mypy`) and tell you what needs to be fixed. You may need to run it more than once. It will be automatically run when attempting to commit a change.

### Testing

To run tests:

```shell
pytest
```

For test coverage:

```shell
pytest --cov=mangroup tests/
```
