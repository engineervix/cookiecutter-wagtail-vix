from django.apps import AppConfig


class BaseConfig(AppConfig):
    name = "{{cookiecutter.project_slug}}.base"
