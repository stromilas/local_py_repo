# How to replicate

### This works:

1. In _/services/api/src_ run `poetry install`. This will install local module located in _/modules/core_.
2. In _/services/api/src_ run `poetry shell`. This will activate virtual environment.
3. Run `npm start` to start development

### This doesn't work:

1. Run `npm run deploy` to deploy the code

### Note

This uses [poetry](https://python-poetry.org/docs/#installation), version 1.1.10
