# Configuration

Here, we'll highlight some important custom configurations for the project as well as third party integrations / apps.

??? tip

    Many of the things discussed here are configured as part of the project's [Django Settings](https://docs.djangoproject.com/en/5.0/topics/settings/). The [settings files](./project-structure.md#settings) themselves are well documented, with links to either the official Django docs or third-party package docs where applicable.

## Media storage

_{{ cookiecutter.project_name }}_ uses [django-storages](https://django-storages.readthedocs.io/en/latest/index.html) in production, and is configured to use an [S3-compatible](https://www.techtarget.com/searchstorage/tip/How-to-use-S3-compatible-storage) object-storage such as [Backblaze B2](https://www.backblaze.com/b2/docs/s3_compatible_api.html).

???+ note

    We use this kind of setup for the following reasons:

    1. **Data Persistence**: [Containers](https://www.docker.com/resources/what-container/) are ephemeral by nature, and any data stored within them can be lost when the container is stopped or restarted. Storing media files locally within a Docker container makes it challenging to persist those files. Django Storages allows you to store media files in a more durable and persistent location, ensuring that your files are retained even if containers are replaced or restarted.
    2. **Maintenance**: Managing media files directly within containers can complicate maintenance and updates. Separating media storage from the containerized application simplifies maintenance tasks.
    3. **Efficient Backups**: Storing media files in a cloud-based storage service often includes built-in backup and redundancy features. This ensures that your media files are safe from data loss due to hardware failures or other unforeseen issues.

??? tip

    [Backblaze B2](https://www.backblaze.com/b2/docs/s3_compatible_api.html) is generally cheaper and esier to set up than [AWS S3](https://aws.amazon.com/s3/)[^1]. To use it as a _django-storages_ backend, [read the setup instructions here](https://django-storages.readthedocs.io/en/stable/backends/backblaze-B2.html).

    **Charges**

    - For **storage**, they charge $0.005/GB/Month, the first 10GB of storage is free.
    - For **downloads**, they charge $0.01/GB. The first 1GB of data downloaded each day is free.
    - There are also what they call **transaction** charges – read more about them at <https://www.backblaze.com/cloud-storage/pricing>. Class “B” transactions are $0.004 per 10,000 with 2,500 free per day. Class “C” transactions are $0.004 per 1,000 with 2,500 free per day.

## Database

This project uses [Postgres](https://www.postgresql.org/) throughout its lifecycle, that is, from development to production. Postgres has earned a strong reputation for its proven architecture, reliability, data integrity, robust feature set, extensibility, and the dedication of the open-source community behind the software to consistently deliver performant and innovative solutions.

Using Postgres and Django together offers many benefits:

- Django provides a number of data types that will only work with Postgres.
- Django has `django.contrib.postgres` to make database operations on Postgres.
- Applications that store geographical data need to use Postgres (with the [PostGIS](https://postgis.net/) extension), as [GeoDjango](https://docs.djangoproject.com/en/5.0/ref/contrib/gis/) is only _fully_ compatible with Postgres.
- Postgres has the richest set of features that are supported by Django.

???+ info

    Here are some of the PostgreSQL-specific features supported by Django:

    - [PostgreSQL-specific aggregation functions](https://docs.djangoproject.com/en/5.0/ref/contrib/postgres/aggregates/)
    - [PostgreSQL-specific database constraints](https://docs.djangoproject.com/en/5.0/ref/contrib/postgres/constraints/)
    - [PostgreSQL-specific form fields and widgets](https://docs.djangoproject.com/en/5.0/ref/contrib/postgres/forms/)
    - [PostgreSQL-specific database functions](https://docs.djangoproject.com/en/5.0/ref/contrib/postgres/functions/)
    - [PostgreSQL-specific model indexes](https://docs.djangoproject.com/en/5.0/ref/contrib/postgres/indexes/)
    - [PostgreSQL-specific lookups](https://docs.djangoproject.com/en/5.0/ref/contrib/postgres/lookups/)
    - [Database migration operations](https://docs.djangoproject.com/en/5.0/ref/contrib/postgres/operations/)
    - [Full-text search](https://docs.djangoproject.com/en/5.0/ref/contrib/postgres/search/)
    - [Validators](https://docs.djangoproject.com/en/5.0/ref/contrib/postgres/validators/)

## Sending emails

Sending emails is an important part of _{{ cookiecutter.project_name }}_, and we want to ensure that we are using a reliable system so that there are no issues with email delivery.

As indicated in the project's README, _{{ cookiecutter.project_name }}_ uses [maildev](https://github.com/maildev/maildev) during development to test emails. In production, we recommend using [django-anymail](https://github.com/anymail/django-anymail) and is configuring it with a suitable transactional email service provider, such as [Brevo](https://www.brevo.com/pricing/), [Mailjet](https://www.mailjet.com/pricing/), [Mailgun](https://www.mailgun.com/pricing/), [Sendgrid](https://sendgrid.com/en-us/pricing), [Postmark](https://postmarkapp.com/pricing) and so on.

With so many options for this, the choice is really dependent on the client's preferences and budget. [Mailjet](https://www.mailjet.com/pricing/) is relatively easy to setup, plus it has a [generous free tier](https://www.mailjet.com/pricing/) – you can send 200 emails per day (6,000 emails/month) for free. If you need to send more emails, then the next plan costs $15/month (15,000 emails/month, no daily limit). [Brevo](https://www.brevo.com/pricing/) has an even more generous free tier at 300 emails per day! The next plan is also $15/month, but allows for up to 20,000 emails/month.

Whichever provider you settle for, check the [django-anymail](https://github.com/anymail/django-anymail) docs on how to configure the specified provider. You'll obviously have to update _django-anymail_'s `extras` parameter in `pyproject.toml`, and [update the project dependencies accordingly](https://realpython.com/dependency-management-python-poetry/#handle-poetrylock).

You can of course just use [Django's built-in SMTP backend](https://docs.djangoproject.com/en/5.0/topics/email/#smtp-backend).

## Worker

This project is configured to work with [django-rq](https://github.com/rq/django-rq) to allow fo scheduling background tasks outside the request-response cycle.

During development, there's a `worker` container that starts automatically when you start the containers with `inv up`. You can check its logs via `inv logs worker`, and if you want to follow log output, add the `-f` argument: `inv logs worker -f`.

In production, you'll see from the `Procfile` that there's a command specified for the `worker` process, whose formation is defined in `app.json`.

## Periodic tasks

While periodic tasks can be executed using [RQ](https://python-rq.org/), we recommend using standard cron schedulers as this is simpler and more cost effective. If you're deploying to Heroku, use their [Heroku Scheduler](https://devcenter.heroku.com/articles/scheduler), which is a free addon. If you're deploying to Dokku, use the [Dokku Managed Cron](https://dokku.com/docs/processes/scheduled-cron-tasks/?h=cron#dokku-managed-cron), whose configuration is done in the project's `app.json` file. The configuration, as of the time of writing these docs, looks like this

```json
  "cron": [
    {
      "command": "python manage.py clearsessions", //(1)!
      "schedule": "@daily"
    }
  ],
```

1.  This cleans out expired sessions. See [the docs](https://docs.djangoproject.com/en/5.0/ref/django-admin/#django-admin-clearsessions).

[^1]: However, if you want more fine-grained control and greater flexibility, you probably wanna use [AWS S3](https://aws.amazon.com/s3/).

---
