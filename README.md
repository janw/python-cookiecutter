# Python Cookiecutter

Best practices [cookiecutter](https://github.com/audreyr/cookiecutter) template derived from the one described in this [blogpost](https://sourcery.ai/blog/python-best-practices/). Notable differences are:

- **Uses [Poetry](https://poetry.eustace.io/) instead of Pipenv**
- Adds project metadata to cookiecutter config
- Adds `Dockerfile`
- Excludes development enviroment tools from dev-dependencies (more on that [below](#why-include-only-pytest-in-the-dev-dependencies)
- Moves manual setup steps (git init, virtualenv/dependency setup, pre-commit hook install) to post-generate hook

## Features

- Testing with [pytest](https://docs.pytest.org/en/latest/)
- Formatting with [black](https://github.com/psf/black)
- Import sorting with [isort](https://github.com/timothycrosley/isort)
- Static typing with [mypy](http://mypy-lang.org/)
- Linting with [flake8](http://flake8.pycqa.org/en/latest/)
- Git hooks that run all the above with [pre-commit](https://pre-commit.com/)

## Quickstart

```sh
# Only if you don't have pipx installed / set up
python3 -m pip install pipx
python3 -m pipx ensurepath

# Install all dev environment tools using pipx
pipx install poetry && \
    pipx install cookiecutter && \
    pipx install flake8 && pipx inject flake8 flake8-bugbear && \
    pipx install black && \
    pipx install mypy && \
    pipx install pre-commit && \
    pipx install isort

# Use cookiecutter to create project from this template
pipx run cookiecutter gh:janw/python-cookiecutter

# Enter project directory
cd <repo_name>
```

## Why only Pytest et al. are included in the dev-dependencies

I believe that mixing development tools and a project's dependencies is a bad idea. Even the dev-dependencies are meant for *application* dependencies required to further develop the app and run its test suite—not for developer dependencies to take care of formatting, linting, etc.

Installing the latter within a project's development environment has no added benefit vs. installing them separately, as their functionality and dependencies are entirely independent of the project. There is simply no point in installing flake8 several times as the purpose is the same in any project, unless your project cannot function without the ~bugs~ quirks of a particular version of any of the tools.

The developer is better off setting up their toolset outside and independently of any one project (for example like in the above [Quickstart](#quickstart) section: using [pipx](https://pipxproject.github.io/pipx/)), and avoid creating a project-specific dependency. That also allows for easy machine-wide updates of the tools, and even for other developers to use different tools if they so prefer. After all what counts is the code style matching.
