# python-CI-template

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
* CI:
    * [Travis-CI](https://travis-ci.org/):
    * [Github actions](https://docs.github.com/en/actions):
* CD:
    * Travis

## How to use
### Linting
* Run `black`:
```
black .
```
* Run `flake8`:
```
flake8
```
* Run `mypy`:
```
mypy .
```
* Init `pre-commit`:
```
# Init pre-commit
pre-commit install
```
### Testing
```
# Run pytest and coverage
coverage run -m pytest
# View report of coverage
coverage report
```
### CI


## Project structure:
.
├── .git
├── .gitignore
└── README.md

### Explain:
* .gitignore: ignore files or folders.
* requirements.txt: required packages for running projects.

## Reference:
* [https://medium.com/kaggle-blog/i-trained-a-model-what-is-next-d1ba1c560e26](https://medium.com/kaggle-blog/i-trained-a-model-what-is-next-d1ba1c560e26)
* [https://www.earthdatascience.org/blog/unit-testing-linting-ci-python/](https://www.earthdatascience.org/blog/unit-testing-linting-ci-python/)
