from django.apps import AppConfig


class UsersConfig(AppConfig):
    name = "{{cookiecutter.project_slug}}.users"
    label = "users"
    verbose_name = "Users"
