# Project Structure

## Overview

The _{{ cookiecutter.project_name }}_ directory tree is outlined and annotated below.

```sh
.
├── .babelrc.js # (1)!
├── .dockerignore # (2)!
├── .editorconfig # (3)!
├── .env.sample # (4)!
├── .eslintrc # (5)!
├── .gitattributes # (6)!
├── .github # (7)!
│	 ├── workflows
│	 │	 ├── ...
│	 │	 └── ...
│	 └── renovate.json
├── .gitignore # (8)!
├── .gitlab-ci.yml # (9)!
├── .pre-commit-config.yaml # (10)!
├── .prettierignore # (11)!
├── app.json # (12)!
├── {{cookiecutter.project_slug}} # (30)!
│	 ├── __init__.py
│	 ├── assets
│	 │	 ├── ico
│	 │	 │	 ├── ...
│	 │	 │	 ├── favicon.ico
│	 │	 │	 └── site.webmanifest
│	 │	 ├── img
│	 │	 │	 ├── ...
│	 │	 │	 └── ...
│	 │	 ├── js
│	 │	 │	 ├── main.js
│	 │	 │	 └── ...
│	 │	 └── scss
│	 │	     ├── abstracts
│	 │	     │	 ├── _custom_bootstrap_vars.scss
│	 │	     │	 └── _variables.scss
│	 │	     ├── base
│	 │	     │	 ├── _base.scss
│	 │	     │	 └── _typography.scss
│	 │	     ├── components
│	 │	     │	 ├── ...
│	 │	     │	 └── ...
│	 │	     ├── layout
│	 │	     │	 ├── ...
│	 │	     │	 └── ...
│	 │	     ├── main.scss
│	 │	     ├── pages
│	 │	     │	 ├── ...
│	 │	     │	 └── ...
│	 │	     ├── themes
│	 │	     │	 ├── ...
│	 │	     │	 └── ...
│	 │	     └── vendors
│	 │	         ├── ...
│	 │	         └── ...
│	 ├── conftest.py
│	 ├── core
│	 │	 ├── __init__.py
│	 │	 ├── apps.py
│	 │	 ├── templates
│	 │	 │	 ├── ...
│	 │	 │	 └── ...
│	 │	 ├── tests
│	 │	 │	 ├── __init__.py
│	 │	 │	 ├── ...
│	 │	 │	 └── ...
│	 │	 ├── views.py
│	 │	 └── wagtail_hooks.py
│	 ├── files
│	 ├── home
│	 │	 ├── __init__.py
│	 │	 ├── apps.py
│	 │	 ├── migrations
│	 │	 │	 ├── ...
│	 │	 │	 └── __init__.py
│	 │	 ├── factories.py
│	 │	 ├── models.py
│	 │	 ├── templates
│	 │	 │    └── home
│	 │	 │	     ├── ...
│	 │	 │	     └── ...
│	 │	 └── tests
│	 │	 	 ├── __init__.py
│	 │	 	 ├── ...
│	 │	 	 └── ...
│	 ├── settings
│	 │	 ├── __init__.py
│	 │	 ├── base.py
│	 │	 ├── dev.py
│	 │	 ├── production.py
│	 │	 └── test.py
│	 ├── static
│	 ├── templates
│	 │	 ├── ...
│	 │	 ├── ...
│	 │	 ├── 400.html
│	 │	 ├── 403.html
│	 │	 ├── 404.html
│	 │	 ├── 500.html
│	 │	 ├── base.html
│	 │	 ├── includes
│	 │	 │	 ├── ...
│	 │	 │	 └── ...
│	 │	 ├── wagtailadmin
│	 │	 │	 ├── ...
│	 │	 │	 └── ...
│	 ├── urls.py
│	 ├── users
│	 │	 ├── __init__.py
│	 │	 ├── admin.py
│	 │	 ├── apps.py
│	 │	 ├── factories.py
│	 │	 ├── migrations
│	 │	 │	 ├── ...
│	 │	 │	 └── __init__.py
│	 │	 ├── models.py
│	 │	 └── tests
│	 │	 	 ├── ...
│	 │	 	 └── ...
│	 └── wsgi.py
├── bin  # (13)!
│	 └── post_compile
├── CHANGELOG.md # (14)!
├── Dockerfile # (15)!
├── docker # (16)!
│	 ├── db
│	 │	 ├── Dockerfile
│	 │	 └── create.sql
│	 ├── docker-compose-frontend.yml
│	 └── Procfile
├── docker-compose.yml # (17)!
├── docs # (18)!
│	 ├── ...
│	 └── index.md
├── LICENSE # (19)!
├── manage.py # (20)!
├── mkdocs.yml # (21)!
├── package-lock.json  # (22)!
├── package.json  # (23)!
├── poetry.lock # (24)!
├── Procfile # (25)!
├── pyproject.toml # (26)!
├── README.md # (27)!
├── tasks.py # (28)!
└── webpack.config.js # (29)!
```

1.  A configuration file for [Babel](https://babeljs.io/). See the [Babel configuration docs](https://babeljs.io/docs/configuration#javascript-configuration-files) for more details.

2.  Used to specify files and directories that should be excluded when building a Docker image.

3.  Helps maintain consistent coding styles for multiple developers working on the same project across various editors and IDEs. See <https://editorconfig.org/> for more details.

4.  Example file for environment variables in the project. Provides a reference for the required environment variables that should be defined for the project to function properly (during development).

5.  Configuration file for [ESLint](https://eslint.org/docs/latest/use/configure/).

6.  Refer to <https://git-scm.com/docs/gitattributes>.

7.  Contains configuration files and settings that are specific to the project's interaction with GitHub. This includes [Github Actions](https://github.com/features/actions) workflows and configuration for [renovate](https://renovatebot.com/) – a dependency update tool that helps keep the project's dependencies up-to-date.

8.  Refer to <https://git-scm.com/docs/gitignore>.

9.  [GitLab CI/CD](https://gitlab.com/) configuration file. [Read the docs](https://docs.gitlab.com/ee/ci/yaml/gitlab_ci_yaml.html).

10. [pre-commit](https://pre-commit.com/) configuration file.

11. A configuration file used by [Prettier](https://prettier.io/), a popular code formatting tool.
    Similar to `.gitignore` and `.dockerignore`, the `.prettierignore` file is used to
    specify files and directories that should be excluded from formatting by Prettier.

12. Configuration file used by some deployment platforms,
    such as [Heroku](https://www.heroku.com/) and [Dokku](https://dokku.com/),
    to define and customize the behavior of an application during the deployment process.

13. For scripts, such as those used as part of the deployment process on platforms
    like [Heroku](https://www.heroku.com/) and [Dokku](https://dokku.com/).

14. A chronologically ordered list of the changes made on the project.
    Ideally, this file should not be manually edited, rather, it should automagically
    be updated via `inv bump` (which would only work if you use [conventional commits](https://www.conventionalcommits.org/))

15. See the official Docker [docs](https://docs.docker.com/engine/reference/builder/) for more details.

16. Contains Docker configuration files **used during development**.

17. [Docker Compose](https://docs.docker.com/compose/) configuration **used during development**.

18. Contains this very documentation that you're currently looking at.

19. The terms and conditions under which this project is licensed.

20. See [this section](https://docs.djangoproject.com/en/5.0/ref/django-admin/#django-admin-and-manage-py) of the Django docs.

21. Configuration file for [MkDocs](https://www.mkdocs.org/) – a fast, simple and
    downright gorgeous static site generator that's used to build _{{ cookiecutter.project_name }}_'s technical docs.

22. This file is automatically generated by [`npm`](https://www.npmjs.com/) when a package
    is installed. It records the exact version of every installed dependency, including
    its sub-dependencies and their versions.

23. [`npm`](https://www.npmjs.com/)’s configuration file, a fundamental part of the project's frontend ecosystem and tooling.

24. A key component of managing Python dependencies with [Poetry](https://python-poetry.org/), the `poetry.lock` file is used to lock and record the specific versions of the dependencies required for the project. It is automatically generated by [Poetry](https://python-poetry.org/) and should therefore not be manually edited, unless in special cases, for instance, when resolving merge conflicts.

25. Used to declare and specify the processes (or "tasks") that should be executed by a process
    manager in a web application or service.
    It is commonly used in the context of deploying and running applications on platforms
    like [Heroku](https://www.heroku.com/) and [Dokku](https://dokku.com/).

26. The `pyproject.toml` file was introduced as part of the [Python Enhancement Proposal (PEP) 518](https://peps.python.org/pep-0518/), that specifies how Python projects must specify build dependencies. See <https://pip.pypa.io/en/stable/reference/build-system/pyproject-toml/>.
    In this project, this file contains configurations for [Poetry](https://python-poetry.org/), [black](https://github.com/psf/black),
    [ruff](https://github.com/astral-sh/ruff),
    [committizen](https://github.com/commitizen-tools/commitizen) and
    [djlint](https://www.djlint.com/). All the project's Python dependencies are specified in this file.

27. Contains information about the project, and development setup instructions.

28. This is where [Invoke](https://www.pyinvoke.org/) tasks are defined.

29. Configuration file for [Webpack](https://webpack.js.org/configuration/).

30. This is the main directory where _{{ cookiecutter.project_name }}_'s core code lives.
    This directory contains what you'd typically expect in a Django project –
    the Django apps, templates, URL configuration, Django settings, frontend assets, tests and more.

## A closer look at the `{{cookiecutter.project_slug}}` directory

As mentioned in the overview above, the `{{cookiecutter.project_slug}}` directory is the main directory where _{{ cookiecutter.project_name }}_'s core code lives.

### Django [apps](https://docs.djangoproject.com/en/5.0/ref/applications/#module-django.apps)

!!! warning

    Please ensure that this section is updated whenever changes are made to the apps,
    for instance, when a new app is added, or an existing app is removed.

_{{ cookiecutter.project_name }}_ contains the following apps, listed in alphabetical order:

`core`

: You may have seen this named `utils`[^1] in some projects. It contains various
core functionality that is critical to the project. This would include, for instance

    - [custom Django middleware](https://docs.djangoproject.com/en/5.0/topics/http/middleware/#writing-your-own-middleware)
    - [custom exceptions](https://docs.python.org/3/tutorial/errors.html#user-defined-exceptions)
    - a bunch of utilities and [helpers](https://subscription.packtpub.com/book/programming/9781839218859/3/ch03lvl1sec32/helper-functions)
    - site search
    - and more ... Take a look at the code for more details.

`home`

: Represents functionality for the website homepage.

`users`

: Consists of a custom [user model](https://docs.djangoproject.com/en/5.0/ref/contrib/auth/#user-model).

### Templates

Site-wide templates are in the `{{cookiecutter.project_slug}}/templates` directory. This includes, but is not limited to

- the `base.html` template, which is used as the base for the homepage, authentication, 404 and other templates.
- template [includes](https://docs.djangoproject.com/en/5.0/ref/templates/builtins/#include)
- [error page](https://docs.djangoproject.com/en/5.0/topics/http/views/#customizing-error-views) templates

App-specific templates are in each app's `templates` subdirectory, as [explained in the Django docs](https://docs.djangoproject.com/en/5.0/ref/templates/api/#django.template.loaders.app_directories.Loader).

### Settings

The [Django Settings](https://docs.djangoproject.com/en/5.0/topics/settings/) are in `{{cookiecutter.project_slug}}/settings`. They have been split into 4 modules:

`settings.base`

: The `base` settings module contains the foundational settings that are common across all environments. It includes configurations related to database connections, installed applications, middleware, static files, templates, internationalization settings, and more. This module serves as the starting point for all other settings modules and provides the base configuration for the project.

`settings.dev`

: The `dev` settings module is specific to the development environment. It includes settings that are helpful during development, such as enabling debug mode, displaying detailed error pages, configuring development-specific middleware, and setting up development databases or cache backends. Additionally, it may include settings for local development tools or libraries that are not needed in production.

`settings.production`

: The `production` settings module is designed for the production environment. It includes settings that are optimized for performance, security, and scalability. This module typically includes configurations for production databases, caching systems, static file serving, secure HTTPS settings, logging configurations, and other production-specific optimizations. It ensures that the application is running efficiently and securely in a production environment.

`settings.test`

: The `test` settings module is dedicated to the testing environment. It contains settings used during automated testing, including configurations for test databases, test runners, and additional test-related settings. This module allows developers to define specific settings for running tests, separate from the development or production environments, ensuring a consistent and isolated testing environment.

### Static files

The project's static files[^2] are in `{{cookiecutter.project_slug}}/assets`, which consists of 4 subdirectories as follows

`ico`

: The project's favicons, generated via <https://favicon.io/>.

`img`

: Consists of various images and SVG illustrations, as well as videos and [lottiefiles](https://lottiefiles.com/).

`js`

: JavaScript files or modules used in the project.

`scss`

: This folder holds the [SCSS](https://sass-lang.com/) source files, which are then compiled into regular CSS files that are served to the browser.

This project uses [webpack](https://webpack.js.org/), and the static files are compiled / copied to the `{{cookiecutter.project_slug}}/static` folder, which is the path defined in the [`STATICFILES_DIRS`](https://docs.djangoproject.com/en/5.0/ref/settings/#staticfiles-dirs) setting.

### Media files

During development, user-uploaded files are held in `{{cookiecutter.project_slug}}/media`. This is the path defined in the [`MEDIA_ROOT`](https://docs.djangoproject.com/en/5.0/ref/settings/#std-setting-MEDIA_ROOT) setting. In production, however, _{{ cookiecutter.project_name }}_ is configured to use an [S3-compatible](https://www.techtarget.com/searchstorage/tip/How-to-use-S3-compatible-storage) object-storage such as [Backblaze B2](https://www.backblaze.com/b2/docs/s3_compatible_api.html). This is made possible via [django-storages](https://django-storages.readthedocs.io/en/latest/index.html).

### `conftest.py`

Defines [pytest](https://docs.pytest.org/) fixtures, plugins, and other configuration options. It serves as a central place to share common configurations and resources across multiple tests or test files.

### `urls.py`

Central routing configuration for _{{ cookiecutter.project_name }}_. It is used to map URLs to the corresponding views or endpoints that handle the incoming requests.

### `wsgi.py`

The entry points for running _{{ cookiecutter.project_name }}_ using the WSGI[^3] protocol.

[^1]: See [Stop naming your python modules “utils”](https://breadcrumbscollector.tech/stop-naming-your-python-modules-utils/) for more details. Ironically, there may probably still be some modules named `utils.py` in the project. You've gotta admit that [naming things is hard](https://martinfowler.com/bliki/TwoHardThings.html)!

[^2]: Websites generally need to serve additional files such as images, JavaScript, or CSS. In Django, we refer to these files as “static files”.

[^3]: Web Server Gateway Interface. WSGI is a standard interface between web servers and web applications, allowing them to communicate and work together.
