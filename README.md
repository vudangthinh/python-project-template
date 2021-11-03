# python-project-template
[![Code style: black](https://img.shields.io/badge/code%20style-black-000000.svg)](https://github.com/psf/black)
[![pre-commit](https://img.shields.io/badge/pre--commit-enabled-brightgreen?logo=pre-commit&logoColor=white)](https://github.com/pre-commit/pre-commit)



This repo implements a simple API in Flask.

Support following tools:
* Linting:
    * [Black](https://black.readthedocs.io/en/stable/): re-format code.
    * [Flake8](https://flake8.pycqa.org/en/latest/): check syntax issues.
    * [Mypy](https://github.com/python/mypy): suggest adding types to the function arguments and return types.
    * [Pre-commit](https://pre-commit.com/): allows running hook scripts before commit.
* Testing:
    * [Pytest](https://docs.pytest.org/): unit test tool
    * [Coverage](https://coverage.readthedocs.io/en/6.1.1/): measures code coverage of unit tests
    <!-- * [Codecov](https://about.codecov.io/):   -->
* CI/CD:
    * [Github actions](https://docs.github.com/en/actions): CI/CD tool

## Running linting, testing
### Linting
* Use `black`:
```bash
black .
```
* Use `flake8`:
```bash
flake8
```
* Use `mypy`:
```bash
mypy .
```
* Use `pre-commit`:
```bash
# Install pre-commit in project
pre-commit install
# Uninstall pre-commit in project
pre-commit uninstall
# Run pre-commit hooks against all files
pre-commit run --all-files
```

### Testing
```bash
# Run pytest and coverage
coverage run -m pytest
# View report of coverage
coverage report
```


## Project structure:
```bash
.
├── .github
│   └── workflows
│       └── ci.yml
├── .gitignore
├── README.md
├── pyproject.toml
├── setup.cfg
├── .pre-commit-config.yaml
├── requirements.txt
├── src
│   └── main.py
└── tests
    ├── test_function.py
    └── test_service.py
```
### Explain:
* `.gitignore`: ignore files or folders.
* `requirements.txt`: required packages for running projects.
* `.github/workflows/ci.yml`: workflows file of github actions
* `pyproject.toml`: config for `black`
* `setup.cfg`: config for `flake8` and `mypy`
* `.pre-commit-config.yaml`: hook config for `pre-commit`
* `src/main.py`: source code
* `tests/test_function.py`: unit tests to test function
* `tests/test_service.py`: unit tests to test services

## How to use this code base
1. Clone this repo:
```bash
git clone https://github.com/vudangthinh/python-CI-template.git
```
2. Change its remote:
```bash
git remote set-url origin new.git.url
```
3. Start coding

## Reference:
* [https://medium.com/kaggle-blog/i-trained-a-model-what-is-next-d1ba1c560e26](https://medium.com/kaggle-blog/i-trained-a-model-what-is-next-d1ba1c560e26)
* [https://www.earthdatascience.org/blog/unit-testing-linting-ci-python/](https://www.earthdatascience.org/blog/unit-testing-linting-ci-python/)
