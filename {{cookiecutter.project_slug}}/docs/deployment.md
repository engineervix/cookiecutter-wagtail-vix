# Deployment

_{{ cookiecutter.project_name }}_ can be deployed in any environment where Docker is supported. The `Dockerfile` that ships with this project is production-ready, and you are free to use whatever means you're most comfortable with to deploy the project.

Ideally, it is desirable to go for a simple deployment setup where you don't have to tinker with so much configurations to get the project up and running. You don't want to spend too much time worrying about servers, load balancers, reverse proxies, and so on.

In this documentation, we will consider a production deployment using [Dokku](https://dokku.com/) -- an extensible, open source [Platform as a Service](https://cloud.google.com/learn/what-is-paas) whose goal is to provide a simple, hackable build environment for developers to quickly get their code from their laptops into the cloud.

> Our personal goal is to make the deployment part easy, so all you have to do is worry about writing code.
>
> https://dokku.com/blog/2016/welcome-to-dokku/

!!! note

    This project's Dockerfile has [multiple stages](https://docs.docker.com/develop/develop-images/multistage-build/),
    you therefore need to specify `production` as the target for deployment.

## Environment Variables

Regardless of whether you're using Dokku or not, you need to ensure that you set the following environment variables when deploying the project to production, otherwise the application will fail to run. Please take note of the comments.

```python
# Core Wagtail/Django Settings
ALLOWED_HOSTS           # e.g. app.example.co.zm
WAGTAILADMIN_BASE_URL   # e.g. https://app.example.co.zm
CSRF_TRUSTED_ORIGINS    # e.g. https://app.example.co.zm
DJANGO_SECRET_KEY       # see the `.env.sample` file for examples of how to generate this

# Docker-related settings
PORT                    # should match whatever is set in the project Dockerfile (8000)

# Database (If using Dokku, this is set automatically)
DATABASE_URL

# Redis Cache (If using Dokku, this is set automatically)
REDIS_URL

# Memcached (If using Dokku, this is set automatically)
# **Note**: Memcached is used for caching image renditions
# see <https://docs.wagtail.org/en/stable/advanced_topics/performance.html#cache>
MEMCACHED_URL

# Core Email Settings
DEFAULT_FROM_EMAIL      # e.g. {{ cookiecutter.project_name }} App <no-reply@foo.bar.co.zm>
EMAIL_RECIPIENTS        # e.g. Jane Doe <jane@example.co.zm>,tech@example.co.zm

# Frontend Cache (see https://docs.wagtail.org/en/stable/reference/contrib/frontendcache.html#cloudflare)
# we assume you're using Cloudflare. If you are using something else update
# `{{cookiecutter.project_slug}}/settings/production.py` accordingly
CLOUDFLARE_BEARER_TOKEN
CLOUDFLARE_DOMAIN_ZONE_ID

# --- Third-Party Services --- #

## 1. AWS S3 / S3-Compatible Storage (e.g backblaze.com)
AWS_ACCESS_KEY_ID       # this should be the application key id for your bucket
AWS_S3_ENDPOINT_URL     # e.g. https://bucket-name.s3.eu-central-003.backblazeb2.com
AWS_S3_REGION_NAME      # e.g. eu-central-003
AWS_SECRET_ACCESS_KEY   # application key for your bucket
AWS_STORAGE_BUCKET_NAME

## 2. Transactional Email Providers
## (configure django-anymail with a selected provider, or use built-in SMTP Backend)

### Example 1: Mailjet
MAILJET_API_KEY
MAILJET_SECRET_KEY

### Example 2: Brevo
SENDINBLUE_API_KEY

### Example 3: Built-in SMTP (You'll need to configure this in `{{cookiecutter.project_slug}}/settings/production.py`)
EMAIL_HOST              # e.g. smtp.example.co.zm
EMAIL_USE_TLS           # e.g. False
EMAIL_PORT              # e.g. 465
EMAIL_USE_SSL           # e.g. True
EMAIL_HOST_USER         # e.g. it-support@example.co.zm
EMAIL_HOST_PASSWORD

## 3. Error Tracking with Sentry (https://sentry.io/)
SENTRY_DSN              # e.g. https://12345678abc@example.ingest.sentry.io/123456
SENTRY_ENVIRONMENT      # e.g. production
```

## System Requirements

Please see the [Dokku System Requirements](https://dokku.com/docs/getting-started/installation/#system-requirements).

We recommend setting up a fresh Ubuntu LTS installation using https://github.com/engineervix/pre-dokku-server-setup/. Once you do that, you can then install Dokku as described in the official docs.

## Dokku Project Setup

_{{ cookiecutter.project_name }}_ is configured out-of-the-box to run on [Heroku](https://www.heroku.com/) / [Dokku](https://dokku.com/) or similar[^1] [PaaS](https://www.techtarget.com/searchcloudcomputing/definition/Platform-as-a-Service-PaaS) setups. The following files constitute an important part of the deployment setup. We've already talked about them in [Project Structure](./project-structure.md):

- `Dockerfile`
- `Procfile`
- `app.json`
- `bin/post_compile`

Once you have your server all set up and Dokku installed, you can proceed to setup _{{ cookiecutter.project_name }}_ on your server. The commands below are executed on your server, unless otherwise stated. See the notes in the comments. Replace the example values / names with the actual ones.

```bash
# if you want to run docker without sudo (Log out and log back in so that your group membership is re-evaluated)
sudo usermod -aG docker "$(whoami)"

# 1. create your app
sudo dokku apps:create {{cookiecutter.project_slug|replace('_', '-')}}

# 2. add a domain to your app
sudo dokku domains:add {{cookiecutter.project_slug|replace('_', '-')}} app.example.co.zm
## check domains report
sudo dokku domains:report {{cookiecutter.project_slug|replace('_', '-')}}
sudo dokku domains:report --global

# 3. setup postgres service | https://github.com/dokku/dokku-postgres
sudo dokku plugin:install https://github.com/dokku/dokku-postgres.git postgres
sudo dokku postgres:create postgres-{{cookiecutter.project_slug|replace('_', '-')}} --image "postgis/postgis" --image-version "15-3.4"
sudo dokku postgres:link postgres-{{cookiecutter.project_slug|replace('_', '-')}} {{cookiecutter.project_slug|replace('_', '-')}}
## Note: DATABASE_URL is automagically set for you, so no need to worry about it

# 4. set up authentication for **backups** on the postgres service
## Datastore backups are supported via AWS S3 and S3 compatible services
## like https://github.com/minio/minio and https://www.backblaze.com/b2/cloud-storage.html
## sudo dokku postgres:backup-auth <service> <aws-access-key-id> <aws-secret-access-key> <aws-default-region> <aws-signature-version> <endpoint-url>
sudo dokku postgres:backup-auth postgres-{{cookiecutter.project_slug|replace('_', '-')}} YOUR-BACKBLAZE-APPLICATION-KEY-ID YOUR-BACKBLAZE-APPLICATION-KEY eu-central-003 v4 https://s3.eu-central-003.backblazeb2.com
## postgres:backup postgres-{{cookiecutter.project_slug|replace('_', '-')}} <bucket-name>
sudo dokku postgres:backup postgres-{{cookiecutter.project_slug|replace('_', '-')}} YOUR-BUCKET-NAME-HERE
## everyday at 4:30AM, 12:30AM, 8:30 PM
sudo dokku postgres:backup-schedule postgres-{{cookiecutter.project_slug|replace('_', '-')}} "30 4,12,20 * * *" YOUR-BUCKET-NAME-HERE
## check: cat the contents of the configured backup cronfile for the service
sudo dokku postgres:backup-schedule-cat postgres-{{cookiecutter.project_slug|replace('_', '-')}}

# 5. setup redis service | https://github.com/dokku/dokku-redis
## https://tute.io/install-setup-redis-dokku
sudo dokku plugin:install https://github.com/dokku/dokku-redis.git redis
sudo dokku redis:create redis-{{cookiecutter.project_slug|replace('_', '-')}}
sudo dokku redis:link redis-{{cookiecutter.project_slug|replace('_', '-')}} {{cookiecutter.project_slug|replace('_', '-')}}
## Note: REDIS_URL is automagically set for you, so no need to worry about it

# 6. setup memcached | https://github.com/dokku/dokku-memcached
sudo dokku plugin:install https://github.com/dokku/dokku-memcached.git memcached
sudo dokku memcached:create memcached-{{cookiecutter.project_slug|replace('_', '-')}}
sudo dokku memcached:link memcached-{{cookiecutter.project_slug|replace('_', '-')}} {{cookiecutter.project_slug|replace('_', '-')}}
# MEMCACHED_URL is automagically set

# 7. set env variables for your app
## Core Wagtail/Django Settings
sudo dokku config:set --no-restart {{cookiecutter.project_slug|replace('_', '-')}} ALLOWED_HOSTS=app.example.co.zm
sudo dokku config:set --no-restart {{cookiecutter.project_slug|replace('_', '-')}} WAGTAILADMIN_BASE_URL=https://app.example.co.zm
sudo dokku config:set --no-restart {{cookiecutter.project_slug|replace('_', '-')}} CSRF_TRUSTED_ORIGINS=https://app.example.co.zm
sudo dokku config:set --no-restart {{cookiecutter.project_slug|replace('_', '-')}} DJANGO_SECRET_KEY=abcdefghijklmnopqrstuvwxyz1234567890

## Docker-related settings
sudo dokku config:set --no-restart {{cookiecutter.project_slug|replace('_', '-')}} PORT=8000

## Core Email Settings
sudo dokku config:set --no-restart {{cookiecutter.project_slug|replace('_', '-')}} DEFAULT_FROM_EMAIL='{{ cookiecutter.project_name }} App <no-reply@foo.bar.co.zm>'
sudo dokku config:set --no-restart {{cookiecutter.project_slug|replace('_', '-')}} EMAIL_RECIPIENTS='Jane Doe <jane@example.co.zm>,tech@example.co.zm'

## Frontend cache
sudo dokku config:set --no-restart {{cookiecutter.project_slug|replace('_', '-')}} CLOUDFLARE_BEARER_TOKEN=foo
sudo dokku config:set --no-restart {{cookiecutter.project_slug|replace('_', '-')}} CLOUDFLARE_DOMAIN_ZONE_ID=bar

## --- Third-Party Services --- #

### A. S3-Compatible Storage (use backblaze.com and choose EU region)
sudo dokku config:set --no-restart {{cookiecutter.project_slug|replace('_', '-')}} AWS_ACCESS_KEY_ID=theapplicationkeyidforyourbucket
sudo dokku config:set --no-restart {{cookiecutter.project_slug|replace('_', '-')}} AWS_S3_ENDPOINT_URL=https://yourbucket.s3.eu-central-003.backblazeb2.com
sudo dokku config:set --no-restart {{cookiecutter.project_slug|replace('_', '-')}} AWS_S3_REGION_NAME=eu-central-003
sudo dokku config:set --no-restart {{cookiecutter.project_slug|replace('_', '-')}} AWS_SECRET_ACCESS_KEY=applicationkeyforyourbucket
sudo dokku config:set --no-restart {{cookiecutter.project_slug|replace('_', '-')}} AWS_STORAGE_BUCKET_NAME=yourbucket

### B. Transactional Email Providers (choose your preferred provider, or use the built-in SMTP Backend)

#### Example 1: Mailjet
sudo dokku config:set --no-restart {{cookiecutter.project_slug|replace('_', '-')}} MAILJET_API_KEY=whatever
sudo dokku config:set --no-restart {{cookiecutter.project_slug|replace('_', '-')}} MAILJET_SECRET_KEY=whatever

#### Example 2: Brevo
sudo dokku config:set --no-restart {{cookiecutter.project_slug|replace('_', '-')}} SENDINBLUE_API_KEY=whatever

#### Example 3: SMTP
sudo dokku config:set --no-restart {{cookiecutter.project_slug|replace('_', '-')}} EMAIL_HOST=smtp.example.co.zm
sudo dokku config:set --no-restart {{cookiecutter.project_slug|replace('_', '-')}} EMAIL_USE_TLS=False
sudo dokku config:set --no-restart {{cookiecutter.project_slug|replace('_', '-')}} EMAIL_PORT=465
sudo dokku config:set --no-restart {{cookiecutter.project_slug|replace('_', '-')}} EMAIL_USE_SSL=True
sudo dokku config:set --no-restart {{cookiecutter.project_slug|replace('_', '-')}} EMAIL_HOST_USER=it-support@example.co.zm
sudo dokku config:set --no-restart {{cookiecutter.project_slug|replace('_', '-')}} EMAIL_HOST_PASSWORD=password

### C. Error Tracking with Sentry (https://sentry.io/)
sudo dokku config:set --no-restart {{cookiecutter.project_slug|replace('_', '-')}} SENTRY_DSN=https://12345678abc@example.ingest.sentry.io/123456
sudo dokku config:set --no-restart {{cookiecutter.project_slug|replace('_', '-')}} SENTRY_ENVIRONMENT=production

# 8. customize Docker Build-time configuration variables
## https://dokku.com/docs/deployment/builders/dockerfiles/#build-time-configuration-variables
sudo dokku docker-options:add {{cookiecutter.project_slug|replace('_', '-')}} build '--target production'

# 9. NGIИX
sudo ufw allow 'Nginx Full'
sudo rm -fv /etc/nginx/sites-enabled/default
sudo systemctl restart nginx
sudo dokku nginx:validate-config
sudo dokku nginx:show-config {{cookiecutter.project_slug|replace('_', '-')}}
### Customize Nginx | set `client_max_body_size`, to make upload feature work better in Django project, for example
sudo dokku nginx:set {{cookiecutter.project_slug|replace('_', '-')}} client-max-body-size 50m
### https://dokku.com/docs/networking/proxies/nginx/#hsts-header
sudo dokku nginx:set {{cookiecutter.project_slug|replace('_', '-')}} hsts-preload true
### regenerate config
sudo dokku proxy:build-config {{cookiecutter.project_slug|replace('_', '-')}}

# 10. SSL
## if your domain is on cloudflare, you need to disable Cloudflare's proxying behavior on your domain
## while you get Let's Encrypt set up on Dokku (https://spiffy.tech/dokku-with-lets-encrypt-behind-cloudflare)
sudo dokku plugin:install https://github.com/dokku/dokku-letsencrypt.git
sudo dokku config:set --no-restart --global DOKKU_LETSENCRYPT_EMAIL=tech@example.co.zm
sudo dokku letsencrypt:set {{cookiecutter.project_slug|replace('_', '-')}} email {{cookiecutter.project_slug|replace('_', '-')}}@example.co.zm
sudo dokku letsencrypt:enable {{cookiecutter.project_slug|replace('_', '-')}}
# this would setup cron job to update letsencrypt certificate
sudo dokku letsencrypt:cron-job --add

# 11. Ports
## check port mappings
sudo dokku proxy:ports {{cookiecutter.project_slug|replace('_', '-')}}
## you may need to set ports if not already set (dokku uses port 5000 by default, but we're using 8000)
sudo dokku ports:remove {{cookiecutter.project_slug|replace('_', '-')}} http:80:5000
sudo sudo dokku ports:add {{cookiecutter.project_slug|replace('_', '-')}} http:80:8000
sudo dokku ports:remove {{cookiecutter.project_slug|replace('_', '-')}} https:443:5000
sudo sudo dokku ports:add {{cookiecutter.project_slug|replace('_', '-')}} https:443:8000

# 12. (on local machine) add a remote origin `dokku` (or whatever you want to name it) to your git repo, and deploy 🚀
# git remote add dokku dokku@your-server:{{cookiecutter.project_slug|replace('_', '-')}}
# the left main: is your branch, the right :main is the target branch on the Dokku server
# git push dokku main:main

# 13. Some Technical Reference / Useful Tips

## 13.1 run a one-off command under an app, e.g. Django shell:
### dokku run {{cookiecutter.project_slug|replace('_', '-')}} python manage.py shell_plus
###   This will start a new container and run the desired command within that container.
###   The container image will be the same container image as was used to start the currently deployed app.
###   As of v0.25.0, this container will be removed after the process exits.

## 13.2 Pretty-print an app or global environment
### dokku config:show {{cookiecutter.project_slug|replace('_', '-')}}
### dokku config:show --global

# 13.3. In order to run `dokku` command without sudo
sudo visudo /etc/sudoers
## then add the following (a comment plus a single line)

# # Allow members of group dokku to run Dokku commands
# %dokku ALL=(ALL:ALL) NOPASSWD:SETENV: /usr/bin/dokku

## save the file, exit and then add current user to the dokku group
sudo usermod -a -G dokku "$(whoami)"

## 13.4 storage (Dokku uses up lots of disk space with each build)
### ref: https://github.com/dokku/dokku-mariadb/issues/38
### setup a cron job as current user (`crontab -e`) to cleanup:
### this runs every 12 hours (feel free to adjust according to your needs)
### use https://crontab.guru/ for quick and simple editing of cron schedule expressions
### 0 */12 * * * docker rm -v $(docker ps -a -q -f status=exited)
```

If all goes well, your site should now be live 🚀! Congratulations! ✨🎉

## CI Deployments

You can automate deployments to your [Dokku](https://dokku.com/) server via [GitHub Actions](https://github.com/features/actions) (and other CI/CD pplatforms). See <https://dokku.com/docs/deployment/continuous-integration/github-actions/>, <https://dokku.com/docs/deployment/continuous-integration/gitlab-ci/> or <https://dokku.com/docs/deployment/continuous-integration/generic/> for more details.

[^1]: With [`Procfile`](https://devcenter.heroku.com/articles/procfile) support.
