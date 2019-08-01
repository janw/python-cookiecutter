# {{cookiecutter.project_name}}

{{cookiecutter.project_description}}

## Development Setup

```sh
# Install dependencies
poetry install --dev

# Setup pre-commit and pre-push hooks
pipenv run pre-commit install -t pre-commit
pipenv run pre-commit install -t pre-push
```

## Credits

This package was created with [Cookiecutter](https://github.com/cookiecutter/cookiecutter) and the [janw/python-cookiecutter](https://github.com/janw/python-cookiecutter) project template.
