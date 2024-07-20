# {{ cookiecutter.project_name }}

> {{ cookiecutter.description }}

[![forthebadge](https://forthebadge.com/images/badges/made-with-python.svg)](https://forthebadge.com)

[![python3](https://img.shields.io/badge/python-3.12-brightgreen.svg)](https://python.org/)
[![Node v22](https://img.shields.io/badge/Node-v22-teal.svg)](https://nodejs.org/en/blog/release/v22.0.0)
[![Code style: black](https://img.shields.io/badge/code%20style-black-000000.svg)](https://github.com/psf/black)
[![code style: prettier](https://img.shields.io/badge/code%20style-prettier-ff69b4.svg)](https://prettier.io/)

[![Commitizen friendly](https://img.shields.io/badge/commitizen-friendly-brightgreen.svg)](http://commitizen.github.io/cz-cli/)
[![Conventional Changelog](https://img.shields.io/badge/changelog-conventional-brightgreen.svg)](https://github.com/conventional-changelog)
[![Conventional Commits](https://img.shields.io/badge/Conventional%20Commits-1.0.0-yellow.svg)](https://conventionalcommits.org)

<!-- START doctoc generated TOC please keep comment here to allow auto update -->
<!-- DON'T EDIT THIS SECTION, INSTEAD RE-RUN doctoc TO UPDATE -->

- [Introduction](#introduction)
- [Development](#development)
  - [First things first](#first-things-first)
  - [Getting Started](#getting-started)
  - [Commits, Releases and Changelogs](#commits-releases-and-changelogs)
  - [Tips](#tips)
- [Project Technical Documentation](#project-technical-documentation)
- [Credits](#credits)

<!-- END doctoc generated TOC please keep comment here to allow auto update -->

## Introduction

This is a [Python](https://www.python.org/) project built using [Wagtail](https://wagtail.org/) – a powerful [Django](https://www.djangoproject.com/) Content Management System.

- As with most web projects, the frontend dependencies, tasks, etc. are managed using [Node.js](https://nodejs.org/). This project uses [Webpack](https://webpack.js.org/) to bundle frontend assets.
- Tests via [pytest](https://pytest.org/)
- Linting and formatting:
  - _python_: [Black](https://black.readthedocs.io/) and [ruff](https://github.com/astral-sh/ruff)
  - _frontend_: [ESLint](https://eslint.org/), [Stylelint](https://stylelint.io/), [prettier](https://prettier.io/) and [djLint](https://www.djlint.com/).
- Task execution and automation using [`invoke`](http://www.pyinvoke.org/).
- [Continuous integration (CI)](https://www.atlassian.com/continuous-delivery/continuous-integration) via [Github Actions](https://github.com/features/actions) / [Gitlab CI/CD](https://docs.gitlab.com/ee/ci/).

## Development

### First things first

Start by ensuring that you have Docker and Docker Compose:

```sh
# check that you have docker on your machine
docker -v

# check that you have docker-compose on your machine
docker-compose -v
```

For the best developer experience, you need to have [Python 3.12](https://www.python.org/) and [Poetry](https://python-poetry.org/) installed on your machine. If, for some reason, you have a different python version, you can use [pyenv](https://github.com/pyenv/pyenv) to install multiple python versions on your machine. Once you have Python 3.12 installed, create a [**virtual environment**](https://realpython.com/python-virtual-environments-a-primer/) and install dependencies via `poetry install --with dev,test,docs`.

### Getting Started

Here, we assume that you have `git` on your machine, and that you have created a Python 3.12 virtual environment and installed the development dependencies.

Now, upon cloning this repository (or forking + cloning your fork), navigate to the cloned project directory.

Skip the next step (involving `.env`) if you have just created a new project using the [`cookiecutter-wagtail-vix`](https://github.com/engineervix/cookiecutter-wagtail-vix) project template.

Then create the required `.env` file:

```sh
cp -v .env.sample .env
```

At this point, you might wanna edit `.env` by replacing `CHANGEME!!` with appropriate values, as indicated in the comments above such an environment variable. You can leave the other values as they are.

Now, build the images and spin up the containers:

```sh
inv up --build
```

This is basically the same as running `docker-compose up -d --build`, but is obviously much shorter 😎. The above is made possible by [Invoke](https://www.pyinvoke.org/), which is [used extensively on this project to automate some tasks](#tips). Also note that `inv` is short for `invoke` — the two can be used interchangeably.

Running the above command may take a while, you might wanna grab a cup of tea ☕.

> **Note**
>
> every time you want to spin up the containers, you can just run `inv up` without specifying the `--build` argument. Only add the `--build` argument if you wanna rebuild the images.

If everything goes well, you should be able to get into the `web` container and access the shell.

```sh
inv exec web bash
```

Once you're in the container,

- apply database migrations via `./manage.py migrate`,
- [create a cache table](https://docs.djangoproject.com/en/5.0/topics/cache/#creating-the-cache-table) via `./manage.py createcachetable`
- create a `superuser` via `./manage.py createsuperuser`,
- run the following to simultaneously launch the [django development server](https://docs.djangoproject.com/en/5.0/ref/django-admin/#django-admin-runserver) and the [webpack dev server](https://webpack.js.org/configuration/dev-server/):

```sh
inv start
```

You can access the dev server at <http://127.0.0.1:8000>. This project uses [MailDev](https://github.com/maildev/maildev) for viewing and testing emails generated during development. The `MailDev` server is accessible at <http://127.0.0.1:1080>.

### Commits, Releases and Changelogs

This project follows the [Conventional Commits](https://www.conventionalcommits.org/en/v1.0.0/) specification for structured and [semantic](https://semver.org/spec/v2.0.0.html) commit messages. It also utilizes a [conventional changelog](https://github.com/conventional-changelog/conventional-changelog#getting-started) to keep track of changes and releases in a standardized way.

Creating a release is as simple as running

```bash
inv bump main
```

Assuming you are working with the `main` branch.

If it's your first release:

```bash
inv bump main --first
```

This will

- create a `v0.0.0` and a `v0.1.0` tag
- update the changelog accordingly
- push the changes to your origin and create a release, complete with release notes.

For the first release, you can also supply the `--major` argument and this will create a `v1.0.0` tag instead of `v0.1.0`

### Tips

- Run `invoke -l` to see all available [Invoke](https://www.pyinvoke.org/) tasks. These are defined in the [tasks.py](tasks.py) file.
- You'll want to setup [pre-commit](https://pre-commit.com/) by running `pre-commit install` followed by `pre-commit install --hook-type commit-msg`. Optionally run `pre-commit run --all-files` to make sure your pre-commit setup is okay.
- You'll probably also want to install Node.js 22 on your machine, together with the dependencies. We recommend using [fnm](https://github.com/Schniz/fnm) or [volta](https://volta.sh/) to simplify managing Node.js versions on your machine.

## Project Technical Documentation

The project's documentation is powered by [mkdocs](https://www.mkdocs.org/), and lives in the [`docs`](./docs/) directory.

You can view it by running the following in the `web` container:

```bash
mkdocs serve
```

The documentation will be available at: <http://127.0.0.1:8001/>

## Credits

This project was created with [Cookiecutter](https://github.com/audreyr/cookiecutter) and the [`engineervix/cookiecutter-wagtail-vix`](https://github.com/engineervix/cookiecutter-wagtail-vix) project template.

---
