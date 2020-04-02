# -*- coding: utf-8 -*-

import sys

project_slug = "{{ cookiecutter.project_slug }}"
if hasattr(project_slug, "isidentifier"):
    assert (
        project_slug.isidentifier()
    ), "'{}' project slug is not a valid Python identifier.".format(project_slug)

assert (
    project_slug == project_slug.lower()
), "'{}' project slug should be all lowercase".format(project_slug)

assert (
    "\\" not in "{{ cookiecutter.author_name }}"
), "Don't include backslashes in author name."

if (
    "{{ cookiecutter.use_bootswatch }}".lower() == "y"
    and "{{ cookiecutter.bootswatch_theme }}" == "none"
):
    print("You should either select a bootswatch theme or not use bootswatch at all")
    sys.exit(1)

bootswatch_themes = [
    "cerulean",
    "cosmo",
    "cyborg",
    "darkly",
    "flatly",
    "journal",
    "litera",
    "lumen",
    "lux",
    "materia",
    "minty",
    "pulse",
    "sandstone",
    "simplex",
    "sketchy",
    "slate",
    "solar",
    "spacelab",
    "superhero",
    "united",
    "yeti",
]

if (
    "{{ cookiecutter.use_bootswatch }}".lower() == "n"
    and "{{ cookiecutter.bootswatch_theme }}" in bootswatch_themes
):
    print("Since you don't wanna use bootswatch, you cannot select a bootswatch theme")
    sys.exit(1)
