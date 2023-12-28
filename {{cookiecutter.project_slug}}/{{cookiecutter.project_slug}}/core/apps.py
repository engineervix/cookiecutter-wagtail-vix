from django.apps import AppConfig


class CoreConfig(AppConfig):
    name = "{{cookiecutter.project_slug}}.core"
    label = "core"
    verbose_name = "Core"
