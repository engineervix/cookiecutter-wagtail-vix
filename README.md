# cookiecutter-wagtail-vix

[![CircleCI](https://circleci.com/gh/engineervix/cookiecutter-wagtail-vix/tree/master.svg?style=svg)](https://circleci.com/gh/engineervix/cookiecutter-wagtail-vix/tree/master)
[![Coverage Status](https://coveralls.io/repos/github/engineervix/cookiecutter-wagtail-vix/badge.svg?branch=master)](https://coveralls.io/github/engineervix/cookiecutter-wagtail-vix?branch=master)
[![python3](https://img.shields.io/badge/python-3.6%20%7C%203.7%20%7C%203.8-brightgreen.svg)](https://python3statement.org/#sections50-why)
[![Requirements Status](https://requires.io/github/engineervix/cookiecutter-wagtail-vix/requirements.svg?branch=master)](https://requires.io/github/engineervix/cookiecutter-wagtail-vix/requirements/?branch=master)
[![Code style: black](https://img.shields.io/badge/code%20style-black-000000.svg)](https://github.com/psf/black)
[![pre-commit](https://img.shields.io/badge/pre--commit-enabled-brightgreen?logo=pre-commit&logoColor=white)](https://github.com/pre-commit/pre-commit)
[![License: MIT](https://img.shields.io/github/license/engineervix/cookiecutter-wagtail-vix)](https://github.com/engineervix/cookiecutter-wagtail-vix/LICENSE)

- [cookiecutter-wagtail-vix](#cookiecutter-wagtail-vix)
  - [What is this ❓](#what-is-this-)
  - [:tada: Features](#tada-features)
  - [:wrench: Prerequisites](#wrench-prerequisites)
    - [:anchor: Core](#anchor-core)
    - [🕶 Optional](#-optional)
  - [:computer: Setup](#computer-setup)
    - [⌨️ to get started](#️-to-get-started)
    - [⚙️ other steps](#️-other-steps)
      - [git workflow](#git-workflow)
  - [:+1: Credits](#1-credits)
  - [✍️ To do](#️-to-do)
  - [📋 Reference](#-reference)

## What is this ❓

This is my take on creating a reusable (and heavily opinionated) [Wagtail 2.10](https://docs.wagtail.io/en/stable/releases/2.10.html) / [Django 3.1](https://docs.djangoproject.com/en/3.1/releases/) project skeleton using [cookiecutter](https://github.com/audreyr/cookiecutter).

This cookiecutter template is mostly a reflection of my personal preferences. It does, however, try to employ "best practices", for example, the [12-factor-app](https://12factor.net/) and [Daniel Greenfeld’s **Cookiecutter Django** framework](https://github.com/pydanny/cookiecutter-django). I also got a lot of ideas from some excellent wagtail-based projects, primarily [bvspca](https://github.com/nfletton/bvspca) and [bakerydemo](https://github.com/wagtail/bakerydemo).

Notwithstanding the foregoing, it is nowhere near perfect, and thus remains a work in progress. Contributions and suggestions for improvement are welcome.

## :tada: Features

- A starting point for a CMS-based website project, with
  - a homepage and "About" section, which includes addition of key personnel (with position, bio, social profiles, etc.)
  - a minimal functional blog with simplified categories and tags,
  - a contact page with contact form and location map. Includes SMS support powered by [Nexmo](https://developer.nexmo.com/messaging/sms/overview)
- Tests written using [pytest](https://docs.pytest.org/en/latest/) in conjunction with [pytest-django](https://pytest-django.readthedocs.io/en/latest/) (plus other pytest plugins), [factory_boy](https://factoryboy.readthedocs.io/en/latest/) and [wagtail-factories](https://github.com/mvantellingen/wagtail-factories). Test coverage currently stands at 92%.
- Latest [Bootstrap 4](https://getbootstrap.com/) with additional themes courtesy of [Bootswatch](https://bootswatch.com/).
- [Font Awesome 5 (free)](https://fontawesome.com/icons?m=free) icons.
- [shufflejs](https://vestride.github.io/Shuffle/) — Categorize, sort, and filter a responsive grid of items
- Live reload courtesy of [BrowserSync](https://browsersync.io/).
- [Grunt](https://gruntjs.com/) based workflow, with defined tasks for:
  - copying minified (dist) files of modules listed in package.json "dependencies" field to the `static/vendors` directory,
  - deleting files and directories in the `static/vendors` directory,
  - _uglifying_ javascript files,
  - _minifying_ css files
  - _watching_ for file changes (in conjunction with BrowserSync)
- [django-environ](https://github.com/joke2k/django-environ) — allows you to utilize 12factor inspired environment variables to configure your Django application.
- [django-extensions](https://github.com/django-extensions/django-extensions) — global custom management extensions for the Django Framework. I especially like [`runserver_plus`](https://django-extensions.readthedocs.io/en/latest/runserver_plus.html) (the standard runserver stuff but with the Werkzeug debugger baked in) and [`shell_plus`](https://django-extensions.readthedocs.io/en/latest/shell_plus.html) (Django shell with autoloading of the apps database models and subclasses of user-defined classes).
- [django-recaptcha](https://github.com/praekelt/django-recaptcha)
- [django-debug-toolbar](https://github.com/jazzband/django-debug-toolbar) for use during development
- [django-maintenancemode-2](https://github.com/alsoicode/django-maintenancemode-2) — makes it easy to put your Django site into "maintenance mode", or more technically, return an HTTP 503 response. This project differs slightly from other implementations in that the maintenance mode flag is stored in your database versus settings or an environment variable. If your site is deployed to multiple servers, the centralized database-based maintenance flag makes it a snap to bring them all up or down at once.
- ... There's definitely much more ...

## :wrench: Prerequisites

### :anchor: Core

- A [\*nix](https://en.wikipedia.org/wiki/Unix-like) environment. My preference is Ubuntu (LTS version such as [18.04](https://wiki.ubuntu.com/BionicBeaver/ReleaseNotes))
- [Node.js](https://nodejs.org/) with the following packages installed **globally**:
  - [concurrently](https://github.com/kimmobrunfeldt/concurrently): `npm install -g concurrently`
  - [Browsersync](https://browsersync.io/): `npm install -g browser-sync`
  - [Grunt](https://gruntjs.com/): `npm install -g grunt-cli` (Although I've started migrating to [Gulp](https://gulpjs.com/) ... :smile:)
  - [commitizen](https://github.com/commitizen/cz-cli/): `npm install commitizen -g`
  - [prettier](https://github.com/prettier/prettier/): `npm install prettier -g`
  - [Sass](https://sass-lang.com): `npm install -g sass`
  - [MailDev](https://github.com/maildev/maildev): `npm install -g maildev`
  - [DocToc](https://github.com/thlorenz/doctoc): `npm install -g doctoc`
  - (optional, but recommended to have it installed on your machine) [lite-server](https://github.com/johnpapa/lite-server): `npm install -g lite-server`
- [yarn](https://yarnpkg.com/): See [installation instructions](https://classic.yarnpkg.com/en/docs/install#debian-stable)
- [Python3](https://www.python.org/) (3.6 and above) with [virtualenvwrapper](https://virtualenvwrapper.readthedocs.io/en/latest/), [pyenv](https://github.com/pyenv/pyenv) and ~~[pipev](https://github.com/pypa/pipenv)~~ [pip-tools](https://github.com/jazzband/pip-tools).
- ~~The wagtail search interface relies on [elasticsearch](https://www.elastic.co/downloads/elasticsearch). If you prefer not to run an Elasticsearch server in development or production, there are many hosted services available, including [Bonsai](https://bonsai.io/signup), who offer a free account suitable for testing and development~~. Switched to the [PostgreSQL Backend](https://docs.wagtail.io/en/latest/topics/search/backends.html#postgresql-backend). Therefore, please ensure that Postgres (and PostGIS) are setup on your machine.

### 🕶 Optional

- Continuous Integration is via [GitLab CI](https://docs.gitlab.com/ee/ci/yaml/). You can setup CI using alternative services like [CircleCI](https://circleci.com/), [Travis CI](https://travis-ci.org/), [Jenkins](https://jenkins.io/), etc.
- [VS Code](https://code.visualstudio.com/)

## :computer: Setup

### ⌨️ to get started

1. ensure that you have [cookiecutter](https://github.com/audreyr/cookiecutter) installed on your computer
2. run `cookiecutter https://github.com/engineervix/cookiecutter-wagtail-vix.git` in your favourite shell. You’ll be prompted for some values, such as **project_name**, , **project_slug**, **email**, **wagtail_username** etc. A new wagtail project will be created in a folder named according to the **project_slug** at your current location.
3. create a virtual environment for your project. `cd` into the project folder created above and install python dependencies: `pip install -r requirements`.
4. Now would be a good time to setup your postgres/postgis database and ensure that you update `DATABASE_URL` and the other environment variables in your `.env` files. The essential ones for starters are `RECAPTCHA_PUBLIC_KEY`, `RECAPTCHA_PRIVATE_KEY` and `MAPBOX_ACCESS_TOKEN`.
5. `export ENV_PATH=.envs/.dev.env`
6. `./manage.py migrate`
7. `./manage.py createsuperuser`. When prompted for a username, please use the **wagtail_username** you specified in step 2. This is important to ensure that you don't have issues when populating the database with initial data, which is tied to the username provided in step 2.
8. `./manage.py load_initial_data`
9. `yarn`
10. `grunt all`
11. `./manage.py collectstatic`
12. Prior to running tests, check the `package.json` to ensure that you have the correct postgres/postgis settings. Once you're all set, go ahead and run tests: `npm run test`
13. Start the development server: `npm run dev`. Your site should be accessible at `http://127.0.0.1:3000` or `http://localhost:3000`.

### ⚙️ other steps

- setup version control (git) for your generated project
- setup [pre-commit](https://pre-commit.com/):
  1. `pre-commit install`
  2. `pre-commit install --hook-type commit-msg`
  3. Update `.git/hooks/prepare-commit-msg` with the following code:

  ```
  #!/usr/bin/env bash
  exec < /dev/tty && node_modules/.bin/git-cz --hook || true
  ```

  4. `pre-commit run --all-files`

> :exclamation: If you are using pyenv, see <https://github.com/pre-commit/pre-commit/issues/810>. In particular, I found [this explanation](https://github.com/pre-commit/pre-commit/issues/810#issuecomment-424732161) from @thomasfowler and [this comment](https://github.com/pre-commit/pre-commit/issues/810#issuecomment-602770714) from @asottile to be very helpful.

#### git workflow

0. :warning: First, ensure that, before you make any changes, you have pulled the latest changes from remote.
1. Add the file(s) you wanna commit: `git add whatever`
2. `git commit` -- this will run [Commitizen](http://commitizen.github.io/cz-cli/); you'll be prompted to fill in any required fields and your commit messages will be formatted according to [cz-conventional-changelog](https://github.com/commitizen/cz-conventional-changelog) &ndash; a Commitizen adapter which prompts for [conventional changelog](https://github.com/conventional-changelog/conventional-changelog) standard.
3. If there are no issues, push your changes accordingly, otherwise, repeat steps 1 and 2 above until all issues are resolved.

> :exclamation: If you encounter `stylelint` errors, you  might wanna run `npm run css-fix` to try and fix such errors. This is likely to happen on first commit!

> :exclamation: If you make any changes to the structure of your README.md or other markdown files, do `npm run toc` before committing, so that the TOC is updated

## :+1: Credits

- `.gitignore` generated using <https://www.gitignore.io/>
- favicon created using <http://realfavicongenerator.net/>
- Images courtesy of [Unsplash](https://unsplash.com/) and [Pixabay](https://pixabay.com/)
- Placeholder logo courtesy of <https://github.com/pigment/fake-logos>
- <https://loremipsum.io/> for placeholder text
- HTML template based on <https://startbootstrap.com/templates/business-frontpage/>
- _Team_ Section on **About** Page based on <https://startbootstrap.com/snippets/about-team/>
- ... I'll keep updating this ...

## ✍️ To do

- [ ] Make the `Makefile` functional
- [ ] Automate Steps 1 to 10 by adding these in the `post_gen_project` hook or incorporating them in the `Makefile`
- [ ] The cookiecutter prompt asks if you wanna use bootswatch themes. If you say "n", it shouldn't prompt you with another question on which bootswatch theme to use! See [this](https://github.com/polyswarm/participant-template/issues/2) and [that](https://github.com/cookiecutter/cookiecutter/issues/913).
- [X] Write tests and setup CI for this cookiecutter package
- [ ] Improve test coverage for the generated wagtail project
- [ ] Setup browser-based testing and production-level testing
- [ ] Improve the Gitlab CI pipeline for the generated wagtail project
- [ ] Possibly add support for other popular CI options (CircleCI, Travis)
- [ ] Add docker support
- [ ] Add support for different Databases right from the beginning.
- [ ] Add better production-level support (serving static assets, mail, caching, perfomance, task queues, Nginx and uWsgi/Gunicorn configuration, etc.)
- [ ] Add `Gulp` support
- [ ] Improve on code style
- [ ] Generate RSS Feeds from Blog
- [ ] Gotta add those [badges](https://shields.io/) :wink:
- [ ] Add custom `sitemap.xml` and `robots.txt`

## 📋 Reference

The data was dumped as follows:

```bash
./manage.py dumpdata --natural-foreign --indent 2 \
    -e contenttypes -e auth \
    -e wagtailcore.groupcollectionpermission \
    -e wagtailcore.grouppagepermission -e wagtailimages.rendition \
    -e sessions > data.json
```
