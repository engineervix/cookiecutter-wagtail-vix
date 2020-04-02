# cookiecutter-wagtail-vix

This is my take on creating a reusable (and heavily opinionated) [Wagtail 2.8](https://docs.wagtail.io/en/v2.8/releases/2.8.html) / [Django 2.2](https://docs.djangoproject.com/en/2.2/releases/) project skeleton using [cookiecutter](https://github.com/audreyr/cookiecutter).

This cookiecutter template is mostly a reflection of my personal preferences. It does, however, try to employ best practices, for example, the [12-factor-app](https://12factor.net/) and [Daniel Greenfeld’s **Cookiecutter Django** framework](https://github.com/pydanny/cookiecutter-django). I also got a lot of ideas from some excellent wagtail-based projects, primarily [bvspca](https://github.com/nfletton/bvspca) and [bakerydemo](https://github.com/wagtail/bakerydemo).

Notwithstanding the foregoing, it is nowhere near perfect, and thus remains a work in progress. Contributions and suggestions for improvement are welcome.

## :tada: Features

- A starting point for a CMS-based website project, with
  - a homepage and "About" section, which includes addition of key personnel (with position, bio, social profiles, etc.)
  - a minimal functional blog with simplified categories and tags,
  - a contact page with contact form and location map. Includes SMS support powered by [Nexmo](https://developer.nexmo.com/messaging/sms/overview)
- Tests written using [pytest](https://docs.pytest.org/en/latest/) in conjunction with [pytest-django](https://pytest-django.readthedocs.io/en/latest/) (plus other pytest plugins), [factory_boy](https://factoryboy.readthedocs.io/en/latest/) and [wagtail-factories](https://github.com/mvantellingen/wagtail-factories)
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

- A [\*nix](https://en.wikipedia.org/wiki/Unix-like) environment. My preference is the latest LTS version of Ubuntu ([18.04](https://wiki.ubuntu.com/BionicBeaver/ReleaseNotes) at the time of writing this)
- [Node.js](https://nodejs.org/) with the following packages installed **globally**:
  - [concurrently](https://github.com/kimmobrunfeldt/concurrently): `npm install -g concurrently`
  - [Browsersync](https://browsersync.io/): `npm install -g browser-sync`
  - [Grunt](https://gruntjs.com/): `npm install -g grunt-cli` (Although I've started migrating to [Gulp](https://gulpjs.com/) ... :smile:)
- [yarn](https://yarnpkg.com/): See [installation instructions](https://classic.yarnpkg.com/en/docs/install#debian-stable)
- [Python3](https://www.python.org/) (3.6 and above) with [virtualenvwrapper](https://virtualenvwrapper.readthedocs.io/en/latest/), [pyenv](https://github.com/pyenv/pyenv) and [pipev](https://github.com/pypa/pipenv).
- The wagtail search interface relies on [elasticsearch](https://www.elastic.co/downloads/elasticsearch). If you prefer not to run an Elasticsearch server in development or production, there are many hosted services available, including [Bonsai](https://bonsai.io/signup), who offer a free account suitable for testing and development.

### 🕶 Optional

- Continuous Integration is via [GitLab CI](https://docs.gitlab.com/ee/ci/yaml/). You can setup CI using alternative services like [CircleCI](https://circleci.com/), [Travis CI](https://travis-ci.org/), [Jenkins](https://jenkins.io/), etc.
- [VS Code](https://code.visualstudio.com/)

## :computer: Setup

### ⌨️ to get started

1. ensure that you have [cookiecutter](https://github.com/audreyr/cookiecutter) installed on your computer
2. run `cookiecutter https://github.com/engineervix/cookiecutter-wagtail-vix.git` in your favourite shell. You’ll be prompted for some values, such as **project_name**, , **project_slug**, **email**, **wagtail_username** etc. A new wagtail project will be created in a folder named according to the **project_slug** at your current location.
3. `cd` into the project folder created above and run `pipenv sync --dev` followed by `pipenv sync`.
4. `pipenv shell`
5. `export ENV_PATH=.envs/.dev.env`
6. `./manage.py migrate`
7. `./manage.py createsuperuser`. When prompted for a username, please use the **wagtail_username** you specified in step 2. This is important to ensure that you don't have issues when populating the database with initial data, which is tied to the username provided in step 2.
8. `./manage.py load_initial_data`
9. `yarn`
10. `grunt all`
11. Ensure that you update other environment variables in your `.env` files. The essential ones for starters are `RECAPTCHA_PUBLIC_KEY`, `RECAPTCHA_PRIVATE_KEY`, `ELASTICSEARCH_URL` and `MAPBOX_ACCESS_TOKEN`.
12. Run tests: `npm run test`
13. Start the development server: `npm run dev`. Your site should be accessible at `http://127.0.0.1:3000` or `http://localhost:3000`.

### ⚙️ other steps

- setup version control (git) for your generated project
- setup [pre-commit](https://pre-commit.com/): `pre-commit install` and then optionally run against all files: `pre-commit run --all-files`

## :+1: Credits

- `.gitignore` generated using <https://www.gitignore.io/>
- favicon created using <http://realfavicongenerator.net/>
- Images courtesy of [Unsplash](https://unsplash.com/) and [Pixabay](https://pixabay.com/)
- Placeholder logo courtesy of <https://github.com/pigment/fake-logos>
- <https://loremipsum.io/> for placeholder text
- ... I'll keep updating this ...

## ✍️ To do

- [ ] Make the `Makefile` functional
- [ ] Automate Steps 1 to 10 by adding these in the `post_gen_project` hook or incorporating them in the `Makefile`
- [ ] The cookiecutter prompt asks if you wanna use bootswatch themes. If you say "n", it shouldn't prompt you with another question on which bootswatch theme to use! See [this](https://github.com/polyswarm/participant-template/issues/2) and [that](https://github.com/cookiecutter/cookiecutter/issues/913).
- [ ] Write tests and setup CI for this cookiecutter package
- [ ] Improve test coverage for the generated wagtail project
- [ ] Setup browser-based testing and production-level testing
- [ ] Improve the Gitlab CI pipeline
- [ ] Possibly add support for other popular CI options (CircleCI, Travis)
- [ ] Add docker support
- [ ] Add support for different Databases right from the beginning.
- [ ] Add better production-level support (serving static assets, mail, caching, perfomance, task queues, Nginx and uWsgi/Gunicorn configuration, etc.)
- [ ] Add `Gulp` support
- [ ] Improve on code style
- [ ] Generate RSS Feeds from Blog
- [ ] Gotta add those [badges](https://shields.io/) :wink:

## 📋 Reference

The data was dumped as follows:

```bash
./manage.py dumpdata --natural-foreign --indent 2 \
    -e contenttypes -e auth \
    -e wagtailcore.groupcollectionpermission \
    -e wagtailcore.grouppagepermission -e wagtailimages.rendition \
    -e sessions > data.json
```
