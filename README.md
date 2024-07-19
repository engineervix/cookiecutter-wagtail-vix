# Welcome to cookiecutter-wagtail-vix 👋

> a minimal, batteries-included, reusable project skeleton to serve as a starting point for a Wagtail project.

[![Continuous Integration](https://github.com/engineervix/cookiecutter-wagtail-vix/actions/workflows/main.yml/badge.svg)](https://github.com/engineervix/cookiecutter-wagtail-vix/actions/workflows/main.yml)
[![Coverage Status](https://codecov.io/gh/engineervix/cookiecutter-wagtail-vix/branch/main/graph/badge.svg)](https://codecov.io/gh/engineervix/cookiecutter-wagtail-vix)
[![Updates](https://pyup.io/repos/github/engineervix/cookiecutter-wagtail-vix/shield.svg)](https://pyup.io/repos/github/engineervix/cookiecutter-wagtail-vix/)
[![python 3.12](https://img.shields.io/badge/python-3.12-brightgreen.svg)](https://python.org)
[![Code style: black](https://img.shields.io/badge/code%20style-black-000000.svg)](https://github.com/psf/black)

[![License: MIT](https://img.shields.io/github/license/engineervix/cookiecutter-wagtail-vix)](https://github.com/engineervix/cookiecutter-wagtail-vix/LICENSE)
![GitHub commits since latest release (by SemVer including pre-releases)](https://img.shields.io/github/commits-since/engineervix/cookiecutter-wagtail-vix/latest)
![GitHub last commit (branch)](https://img.shields.io/github/last-commit/engineervix/cookiecutter-wagtail-vix/main)

[![Commitizen friendly](https://img.shields.io/badge/commitizen-friendly-brightgreen.svg)](http://commitizen.github.io/cz-cli/)
[![Conventional Commits](https://img.shields.io/badge/Conventional%20Commits-1.0.0-blue.svg)](https://conventionalcommits.org)
[![Conventional Changelog](https://img.shields.io/badge/changelog-conventional-brightgreen.svg)](https://github.com/conventional-changelog)

<!-- START doctoc generated TOC please keep comment here to allow auto update -->
<!-- DON'T EDIT THIS SECTION, INSTEAD RE-RUN doctoc TO UPDATE -->

**Contents** _generated with [DocToc](https://github.com/thlorenz/doctoc)_

- [Introduction](#introduction)
- [Features ✨](#features-)
- [Getting Started 🚀](#getting-started-)
  - [A note regarding django-rq](#a-note-regarding-django-rq)
- [Contributing 🤝](#contributing-)
- [Show your support 🙌](#show-your-support-)
- [Credits 👏](#credits-)
- [Author 🧑‍💻](#author-)
- [License 📝](#license-)

<!-- END doctoc generated TOC please keep comment here to allow auto update -->

<p align="center">
  <img src="https://github.com/engineervix/cookiecutter-wagtail-vix/blob/main/docs/img/screenshot.png" alt="Screenshot">
</p>

## Introduction

Embarking on any project "from scratch" is a formidable undertaking, entailing intricate configurations and setup that can quickly become overwhelming. Whether it's the time-consuming task of handling dependencies, structuring the project, or setting up a cohesive development environment – the challenges are universal.

Enter `cookiecutter-wagtail-vix` – a template crafted to simplify the kick-off of [Wagtail](https://wagtail.org/) projects. This template is designed to streamline the setup process, sparing you from the headaches that often accompany the early stages of a project. By starting your new [Wagtail](https://wagtail.org/) project using `cookiecutter-wagtail-vix`, you leapfrog the tedious setup tasks, allowing you to focus on what truly matters – crafting your project's unique functionality with ease.

## Features ✨

Here are some key highlights:

- Tech stack
  - Docker
  - Python 3.12, with Poetry for dependency management, and [Black](https://black.readthedocs.io/) + [ruff](https://github.com/astral-sh/ruff) for formatting and linting.
  - Django 5.0
  - Wagtail 6.1
  - Node.js 22, with [Webpack](https://webpack.js.org/) 5 to bundle frontend assets
- A good starting point for any Wagtail project, with essential batteries included and very minimal assumptions on what you are building.
- Production-ready setup, so you don't waste time going from development to production.
- Includes 3 Django apps to start with:
  - `home`: Has a `HomePage` model which just extends the Wagtail `Page` model and does nothing else. This gives you freedom to set it up as you please.
  - `core`: has **search** functionality and [wagtail-font-awesome-svg](https://github.com/wagtail-nest/wagtail-font-awesome-svg) configuration. The idea is to use this app for global functions, utilities, etc. Feel free to rename it to `utils` or `utilities` if you like!
  - `users`: Custom User model as [recommended in the Django docs](https://docs.djangoproject.com/en/5.0/topics/auth/customizing/#using-a-custom-user-model-when-starting-a-project). The model just extends `AbstractUser` and does nothing else, so you can customise it as you please.
- Ready to run background tasks via [Django-RQ](https://github.com/rq/django-rq):
  - The [`django-rq`](https://github.com/rq/django-rq) package is installed, and all the configuration available, though commented out. Please see [note below](#a-note-regarding-django-rq).
- Custom [Bootstrap 5](https://getbootstrap.com/) Compilation using Sass. No other frontend dependencies.
- Configured to work with [pytest](https://docs.pytest.org/en/latest/) in conjunction with [pytest-django](https://pytest-django.readthedocs.io/en/latest/) (plus other pytest plugins), [factory_boy](https://factoryboy.readthedocs.io/en/latest/) and [wagtail-factories](https://github.com/wagtail/wagtail-factories). You have a starting test coverage of 100%! Ain't that great?
- Task execution and automation using [`invoke`](http://www.pyinvoke.org/).
- Includes some useful packages to boost your DX and productivity, for instance:
  - [django-crispy-forms](https://github.com/django-crispy-forms/django-crispy-forms) + [crispy-bootstrap5](https://github.com/django-crispy-forms/crispy-bootstrap5)
  - [django-debug-toolbar](https://github.com/jazzband/django-debug-toolbar) for use during development
  - [django-environ](https://github.com/joke2k/django-environ) — allows you to utilize 12factor inspired environment variables to configure your Django application.
  - [django-extensions](https://github.com/django-extensions/django-extensions) — global custom management extensions for the Django Framework. I especially like [`shell_plus`](https://django-extensions.readthedocs.io/en/latest/shell_plus.html) (Django shell with autoloading of the apps database models and subclasses of user-defined classes).
  - [django-widget-tweaks](https://github.com/jazzband/django-widget-tweaks), which allows you to tweak the form field rendering in templates, not in python-level form definitions.
  - [django-storages](https://github.com/jschneier/django-storages) — provides a variety of storage backends
  - [whitenoise](https://github.com/evansd/whitenoise) — simplified static file serving for Python web apps
- Linting and formatting:
  - _python_: [Black](https://black.readthedocs.io/) and [ruff](https://github.com/astral-sh/ruff)
  - _frontend_: [ESLint](https://eslint.org/), [Stylelint](https://stylelint.io/), [prettier](https://prettier.io/) and [djLint](https://www.djlint.com/).
- Detailed documentation via [MkDocs](https://www.mkdocs.org/)
- A minimal, ready to use VSCode configuration, just update the path to your python executable in the generated `.vscode/settings.json`.
- [Continuous integration (CI)](https://www.atlassian.com/continuous-delivery/continuous-integration) via [Github Actions](https://github.com/features/actions) / [Gitlab CI/CD](https://docs.gitlab.com/ee/ci/).
- Automatic dependency management via [Renovate](https://github.com/marketplace/renovate) (for Github repos only).

## Getting Started 🚀

In order to generate a new project from this cookiecutter template:

1. ensure that you have [cookiecutter](https://github.com/audreyr/cookiecutter) installed on your computer
2. run `cookiecutter https://github.com/engineervix/cookiecutter-wagtail-vix.git` in your favourite shell. You’ll be prompted for some values, such as **project_name**, **project_slug**, **email** etc. A new wagtail project will be created in a folder named according to the **project_slug** at your current location.
3. Thereafter, `cd` into the project folder created above and follow the instructions in your shiny new project's README.

### A note regarding django-rq

If you would like to run background tasks via [`django-rq`](https://github.com/rq/django-rq), you'll need to make the following changes:

1. in `settings/base.py`

   - uncomment the entry in the `THIRD_PARTY_APPS` list
   - uncomment `RQ_QUEUES`

2. in `settings/production.py`

   - uncomment `RQ_QUEUES`
   - uncomment the commented out items in the `LOGGING` dict

3. in `Procfile`

   - uncomment the `worker` entry

4. in `.env`

   - uncomment the line `RQ_QUEUE=redis://redis:6379/0`

5. in `urls.py`

   - uncomment the line with `path("dj-rq/", include("django_rq.urls")),`

6. in `docker-compose.yml`
   - uncomment the `redis` service entry
   - uncomment the `worker` service entry

## Contributing 🤝

<!-- Thanks goes to these wonderful people ([emoji key](https://allcontributors.org/docs/en/emoji-key)): -->

<!-- ALL-CONTRIBUTORS-LIST:START - Do not remove or modify this section -->
<!-- prettier-ignore-start -->
<!-- markdownlint-disable -->

<!-- markdownlint-restore -->
<!-- prettier-ignore-end -->

<!-- ALL-CONTRIBUTORS-LIST:END -->

This project follows the [all-contributors](https://github.com/all-contributors/all-contributors) specification. Contributions, issues and feature requests are most welcome!

Feel free to check the [issues page](https://github.com/engineervix/cookiecutter-wagtail-vix/issues) and take a look at the [contributing guide](https://github.com/engineervix/cookiecutter-wagtail-vix/blob/main/CONTRIBUTING.md) before you get started.

To maintain code quality and formatting consistency, we utilize pre-commit hooks. These hooks automatically check and format your code before each commit. This helps ensure that the codebase remains clean and consistent throughout the development process. Set up the Git pre-commit hooks by running the following

```bash
pre-commit install && pre-commit install --hook-type commit-msg
```

See `pre-commit-config.yaml` for more details. In addition, please note the following:

- if you're making code contributions, please try and write some tests to accompany your code, and ensure that the tests pass. Also, were necessary, update the docs so that they reflect your changes.
- your commit messages should follow the conventions described [here](https://www.conventionalcommits.org/). Write your commit message in the imperative: "Fix bug" and not "Fixed bug" or "Fixes bug".

Once you are done, please create a [pull request](https://github.com/engineervix/cookiecutter-wagtail-vix/pulls).

## Show your support 🙌

Please give a ⭐️ if this project helped you!

## Credits 👏

- `.gitignore` generated using <https://www.gitignore.io/>
- favicon created using <https://favicon.io/>
- Images courtesy of [Unsplash](https://unsplash.com/) and [Pixabay](https://pixabay.com/)
- Placeholder logo courtesy of <https://github.com/pigment/fake-logos>
- <https://loremipsum.io/> for placeholder text

## Author 🧑‍💻

👤 **Victor Miti**

- Blog: <https://blog.victor.co.zm>
- [![X: engineervix](https://img.shields.io/twitter/follow/engineervix.svg?style=social)](https://twitter.com/engineervix)
- Github: [@engineervix](https://github.com/engineervix)

## License 📝

Copyright © 2020 - 2024 [Victor Miti](https://github.com/engineervix).

This project is licensed under the terms of the [MIT](https://github.com/engineervix/engineervix/blob/main/LICENSE) license.
