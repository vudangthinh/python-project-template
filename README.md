# python-CI-template
[![pre-commit](https://img.shields.io/badge/pre--commit-enabled-brightgreen?logo=pre-commit&logoColor=white)](https://github.com/pre-commit/pre-commit)


This template implements a simple API in Flask.

Support following tools:
* Linting:
    * [Black](https://black.readthedocs.io/en/stable/): re-format code.
    * [Flake8](https://flake8.pycqa.org/en/latest/): check syntax issues.
    * [Mypy](https://github.com/python/mypy): suggest adding types to the function arguments and return types.
    * [Pre-commit](https://pre-commit.com/): run code linting before commit.
* Testing:
    * [Pytest](https://docs.pytest.org/):
    * [Coverage](https://coverage.readthedocs.io/en/6.1.1/)
    <!-- * [Codecov](https://about.codecov.io/):   -->
* CI/CD:
    * [Travis-CI](https://travis-ci.org/):
    * [Github actions](https://docs.github.com/en/actions):

## Running linting, testing, CI/CD
### Linting
* Use `black`:
```
black .
```
* Use `flake8`:
```
flake8
```
* Use `mypy`:
```
mypy .
```
* Use `pre-commit`:
```
# Install pre-commit in project
pre-commit install
# Uninstall pre-commit in project
pre-commit uninstall
# Run pre-commit hooks against all files
pre-commit run --all-files
```

### Testing
```
# Run pytest and coverage
coverage run -m pytest
# View report of coverage
coverage report
```

### CI/CD


## Project structure:
.  
├── .git  
├── .gitignore  
└── README.md  

### Explain:
* .gitignore: ignore files or folders.
* requirements.txt: required packages for running projects.

## How to use this code base
1. Clone this repo:
```
git clone https://github.com/vudangthinh/python-CI-template.git
```
2. Change its remote:
```
git remote set-url origin new.git.url
```
3. Start coding

## Reference:
* [https://medium.com/kaggle-blog/i-trained-a-model-what-is-next-d1ba1c560e26](https://medium.com/kaggle-blog/i-trained-a-model-what-is-next-d1ba1c560e26)
* [https://www.earthdatascience.org/blog/unit-testing-linting-ci-python/](https://www.earthdatascience.org/blog/unit-testing-linting-ci-python/)
