# Maintenance

## Backups

Ensure that you run regular backups of the database. If you're using Dokku, you will see from the [Deployment](./deployment.md) section that we configure automatic periodic backups to a private Backblaze bucket. If, for instance, something went wrong with your server and you had to do a redeployment, you can restore your database from a backup as follows (assuming your postgres database is called `postgres-{{cookiecutter.project_slug|replace('_', '-')}}`)

```bash
# NOTE: your database backup will probably be gzipped, you must extract it
dokku postgres:import postgres-{{cookiecutter.project_slug|replace('_', '-')}} < /path/to/your/databasebackup
```

## Dependencies

_{{ cookiecutter.project_name }}_ has a configuration for [renovate](https://renovatebot.com/) – a dependency update tool that helps keep the project's dependencies up-to-date. If you use GitHub, you should get Pull Requests from the Renovate Bot whenever there are package updates. Security updates will automatically be merged. However, minor updates and major updates may potentially require manual checking and testing before incorporating them into the project, to avoid possibly breaking project functionality. If you are using Gitlab or something else, you'll have to figure out how to setup renovate (or similar tools) there.

## Scaling

Scaling your project is essential as it grows to accommodate increased traffic and user demands. If you have deployed to Dokku, then you'll be happy to know that Dokku provides a flexible and straightforward way to scale your application horizontally and manage multiple instances.

In `app.json`, we've set the default scaling to 1 `web` process and 1 `worker` process. You can increase these if needed. See <https://dokku.com/docs/processes/process-management/#scaling-apps> for more details.

## Logging and Monitoring

_{{ cookiecutter.project_name }}_ is configured to use [Sentry](https://sentry.io/) for application performance monitoring & error tracking. If something goes wrong, it should be captured by Sentry.
