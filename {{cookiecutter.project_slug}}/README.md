# {{ cookiecutter.project_name }}

> {{ cookiecutter.description }}

[![forthebadge](https://forthebadge.com/images/badges/made-with-python.svg)](https://forthebadge.com)

[![python3](https://img.shields.io/badge/python-3.6%20%7C%203.7%20%7C%203.8-brightgreen.svg)](https://python3statement.org/#sections50-why)
[![Code style: black](https://img.shields.io/badge/code%20style-black-000000.svg)](https://github.com/psf/black)
[![Commitizen friendly](https://img.shields.io/badge/commitizen-friendly-brightgreen.svg)](http://commitizen.github.io/cz-cli/)

<!-- START doctoc generated TOC please keep comment here to allow auto update -->
<!-- DON'T EDIT THIS SECTION, INSTEAD RE-RUN doctoc TO UPDATE -->
**Contents**  *generated with [DocToc](https://github.com/thlorenz/doctoc)*

<!-- END doctoc generated TOC please keep comment here to allow auto update -->

## Features ✨

- This is a [Python](https://www.python.org/) project built using [Wagtail](https://wagtail.io/) – a powerful [Django](https://www.djangoproject.com/) Content Management System.
- As with most web projects, the frontend dependencies, tasks, etc. are managed using [Node.js](https://nodejs.org/). This project uses [Yarn](https://yarnpkg.com/) and [Gulp](https://gulpjs.com/)
- [PostgreSQL](https://www.postgresql.org/)/[PostGIS](https://postgis.net/) Database
- [Celery](https://docs.celeryproject.org/en/stable/) Tasks
- [Redis](https://redis.io/) as a fast, persistent cache and Celery backend
- [Google Recaptcha](https://www.google.com/recaptcha/about/) for added security on forms
- [Leaflet](https://leafletjs.com/) and [Mapbox](https://www.mapbox.com/) for maps
<!-- - [Vonage](https://www.vonage.com/) (formerly _Nexmo_) for SMS -->
- [Sendgrid](https://sendgrid.com/) for transactional email
- [Sentry](https://sentry.io) for error tracking in production
- [Memcached](http://memcached.org/) for caching image renditions in production
- [Frontend-cache invalidation](https://docs.wagtail.io/en/stable/reference/contrib/frontendcache.html#frontend-cache-invalidator) using [Cloudflare](https://www.cloudflare.com/)
- Tests via [pytest](https://pytest.org/)
- Linting using [Black](https://black.readthedocs.io/), [Flake8](https://flake8.pycqa.org/) and [isort](https://pycqa.github.io/isort/)
- Task execution and automation using [`invoke`](http://www.pyinvoke.org/).
- [Continuous integration (CI)](https://www.atlassian.com/continuous-delivery/continuous-integration) via [GitHub Actions](https://github.com/features/actions) / [circleCI](https://circleci.com/) / [GitLab CI/CD](https://docs.gitlab.com/ee/ci/).
- Automatic dependency management via [Renovate](https://github.com/marketplace/renovate)

## Development 💻

### First things first

A [\*nix](https://en.wikipedia.org/wiki/Unix-like) environment is highly recommended. Although you can possibly develop on Windows too (if you do, and you're using Powershell or CMD, you'll probably have to adapt some commands to suit a Windows Environment, because these docs assume you're running in a \*nix environment). You need to:

- ensure that [Python 3.6+](https://www.python.org/) is installed on your machine, and that you are able to configure python [**virtual environment**](https://realpython.com/python-virtual-environments-a-primer/)s;
- ensure that you have [git](https://git-scm.com/) setup on your machine;
- install and configure [PostGIS](https://postgis.net/) on your machine.
- install and configure [redis](https://redis.io/) on your development machine.
- Ensure that you have [Node.js 12+](https://nodejs.org/) and [yarn](https://yarnpkg.com/) with the following packages installed **globally**:
  - [Browsersync](https://browsersync.io/): `npm install -g browser-sync`
  - [commitizen](https://github.com/commitizen/cz-cli/): `npm install commitizen -g`
  - [concurrently](https://github.com/kimmobrunfeldt/concurrently): `npm install -g concurrently`
  - [DocToc](https://github.com/thlorenz/doctoc): `npm install -g doctoc`
  - [Gulp](https://gulpjs.com/): `npm install gulp-cli -g`
  - [MailDev](https://github.com/maildev/maildev) – `npm install -g maildev`
  - [prettier](https://github.com/prettier/prettier/): `npm install prettier -g`
  - [Sass](https://sass-lang.com): `npm install -g sass`

Other considerations:

- If you're running Windows, we highly recommend using [Cmder](https://cmder.net/) as your console emulator. It comes bundled with [Git](https://git-scm.com/), and will be less frustrating than using the default Windows console.
- We also recommend using either [VSCode](https://code.visualstudio.com/) or [PyCharm](https://www.jetbrains.com/pycharm/) as your editor. Of course you're free to use whatever editor you want!

### Getting Started

First, [fork](https://docs.github.com/en/free-pro-team@latest/github/getting-started-with-github/fork-a-repo) this repository, then fire up your command prompt and clone the forked repository.

Then, navigate to the cloned project directory: `cd {{cookiecutter.project_slug}}`

Activate your python virtual environment and `pip install --upgrade pip`

Install [pip-tools](https://github.com/jazzband/pip-tools): `pip install pip-tools`.

Run `pip-compile requirements.in` followed by `pip install -r requirements.txt`

Setup [pre-commit](https://pre-commit.com/) by running `pre-commit install` followed by `pre-commit install --hook-type commit-msg`. Optionally run `pre-commit run --all-files` to make sure your pre-commit setup is okay.

Install the Node.js dependencies and copy the vendor libraries to the `static` directory:

```sh
yarn install && gulp cp
```

Create a Postgres/PostGIS database and user for the project. If you are using tools such as [PGAdmin](https://www.pgadmin.org/) or [Postgres.app](https://postgresapp.com/), you please feel free to use them according to their documentation. If you are using the CLI like me, you could do it as follows:

```sh
# assuming your DATABASE is my_DB
# assuming USER is my_user
# assuming your PASSWORD is my_password
psql -c "CREATE USER my_user PASSWORD 'my_password'" \
&& psql -c "CREATE DATABASE my_DB OWNER my_user" \
&& psql -c "GRANT ALL PRIVILEGES ON DATABASE my_DB TO my_user" \
&& psql -c "ALTER ROLE my_user SUPERUSER" \
&& psql -d my_DB -c "CREATE EXTENSION postgis" \
&& psql -d my_DB -c "CREATE EXTENSION postgis_topology"
```

Now that your database is set up, it's time to set up your environment variables. This repo contains a directory `.envs` which has `*.env.sample` files for you to build on and customize. Make copies of these files and remove the `.sample` from the copies:

```sh
# first, rename the `.envs.sample` directory to `.envs`
cp -v .envs/.dev.env.sample .envs/.dev.env
cp -v .envs/.test.env.sample .envs/.testenv
cp -v .envs/.prod.env.sample .envs/.prod.env
```

There are three `.env` files:

1. `.dev.env` – for the **development** environment
2. `.test.env` – for the **test** environment
3. `.prod.env` – for the **production** environment

Edit those files and update the environment variables accordingly. The table below shows the environment variables that need to be updated. For now, you can skip the environment variables for production, and only update them when you are ready to go into production. For starters (development and test), you'll need to:

- generate a `DJANGO_SECRET_KEY` (There are many ways to do this, one of which is suggested in all the `*.env` files). Another quick way is to run `openssl rand -hex 32` in your terminal.
- create a [Google Recaptcha](https://www.google.com/recaptcha/about/) account and obtain the `RECAPTCHA_PUBLIC_KEY` and `RECAPTCHA_PRIVATE_KEY`.
- create a [Mapbox](https://www.mapbox.com/) account and obtain the `MAPBOX_ACCESS_TOKEN`.

|     | development           | test                  | production                |
| --- | --------------------- | --------------------- | ------------------------- |
| 1   | DJANGO_SECRET_KEY     | DJANGO_SECRET_KEY     | DJANGO_SECRET_KEY         |
| 2   | DATABASE_URL          | RECAPTCHA_PUBLIC_KEY  | DATABASE_URL              |
| 3   | RECAPTCHA_PUBLIC_KEY  | RECAPTCHA_PRIVATE_KEY | EMAIL_RECIPIENTS          |
| 4   | RECAPTCHA_PRIVATE_KEY | MAPBOX_ACCESS_TOKEN   | DEFAULT_FROM_EMAIL        |
| 5   | MAPBOX_ACCESS_TOKEN   |                       | ALLOWED_HOSTS             |
| 6   |                       |                       | BASE_URL                  |
| 7   |                       |                       | RECAPTCHA_PUBLIC_KEY      |
| 8   |                       |                       | RECAPTCHA_PRIVATE_KEY     |
| 9   |                       |                       | SENDGRID_API_KEY          |
| 10  |                       |                       | MAPBOX_ACCESS_TOKEN       |
| 11  |                       |                       | NEXMO_API_KEY             |
| 12  |                       |                       | NEXMO_API_SECRET          |
| 13  |                       |                       | NEXMO_DEFAULT_FROM        |
| 14  |                       |                       | CLOUDFLARE_BEARER_TOKEN   |
| 15  |                       |                       | CLOUDFLARE_DOMAIN_ZONE_ID |
| 16  |                       |                       | SENTRY_DSN                |
| 17  |                       |                       | REDIS_KEY_PREFIX          |

Please note that, in production, this project uses

- [Sendgrid](https://sendgrid.com/) for sending emails via [django-anymail](https://github.com/anymail/django-anymail). You can use your preferred provider and update both the [production settings](config/settings/production.py) and environment variables accordingly.
- [Sentry](https://sentry.io) for error tracking.

Okay, now that you have installed all dependencies and have set up your database and environment variables, you can now create database migrations and create the superuser in readiness to run the project:

```sh
# **Important Note**:
# You have to set the `ENV_PATH` variable otherwise you will get an error when you try to run anything.
# Setting this tells Django which environment file to use.
# This can be automated in many ways, as has been done, for example, using yarn/npm scripts.
export ENV_PATH=.envs/.dev.env
./manage.py makemigrations && ./manage.py migrate
./manage.py createsuperuser
```

At this stage, hopefully everything should be working fine, and you should be able to start hacking on the project.

### Tests

Simply run `yarn test` to run tests using `pytest`.

### Code Formatting

- Run `invoke lint` to run [`flake8`](https://flake8.pycqa.org/en/latest/), [`black`](https://black.readthedocs.io/en/stable/), [`isort`](https://pycqa.github.io/isort/) on the code.
- If you get any errors from `black` and/or `isort`, run `invoke lint --fix` or `invoke lint -f` so that black and isort can format your files. If this still doesn't work, don't worry, there's a bunch of pre-commit hooks that that have been set up to deal with this. Take a look at [.pre-commit-config.yaml](.pre-commit-config.yaml).

### Contributing 🤝

Contributions of any kind welcome! Please see [CONTRIBUTING.md](CONTRIBUTING.md) for guidelines on how to contribute. In addition, please note the following:

- if you're making code contributions, please try and write some tests to accompany your code, and ensure that the tests pass. Also, were necessary, update the docs so that they reflect your changes.
- commit your changes via `git commit`. Follow the prompts. When you're done, `pre-commit` will be invoked to ensure that your contributions and commits follow defined conventions. See `pre-commit-config.yaml` for more details.
- your commit messages should follow the conventions described [here](https://www.conventionalcommits.org/en/v1.0.0/). Write your commit message in the imperative: "Fix bug" and not "Fixed bug" or "Fixes bug." This convention matches up with commit messages generated by commands like `git merge` and `git revert`.
  Once you are done, please create a [pull request](https://docs.github.com/en/free-pro-team@latest/github/collaborating-with-issues-and-pull-requests/creating-a-pull-request).

## Running the application 🚀

### without celery

Launch the development server by running:

```sh
yarn dev
```

### with celery

Launch the development server by running:

```sh
yarn dev:celery
```

If all goes well, this will launch two tabs in your default browser – a `maildev` tab and a `django` tab. The [Browsersync](https://browsersync.io/) and [gulp](https://gulpjs.com/) setup provides for automatic restarting of the dev server and autoreload of the browser, so you can work on the project and make changes to the files without having to do this manually. Any emails you send or receive during development will appear in the `maildev` tab. [MailDev](https://github.com/maildev/maildev) provides an excellent way to test emails during development, without having to send actual emails to real email addresses!

## TODO ✅

- [ ] ...
- [ ] ...

## Credits 👏

This project was created with [Cookiecutter](https://github.com/audreyr/cookiecutter) and the [`engineervix/cookiecutter-wagtail-vix`](https://github.com/engineervix/cookiecutter-wagtail-vix) project template.

## Design Notes 📝

...
...
...

---
