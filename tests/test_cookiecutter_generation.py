import os
import re

import pytest
from cookiecutter.exceptions import FailedHookException
import sh
import yaml
from binaryornot.check import is_binary

PATTERN = r"{{(\s?cookiecutter)[.](.*?)}}"
RE_OBJ = re.compile(PATTERN)


@pytest.fixture
def context():
    return {
        "project_name": "Test Wagtail Project",
        "project_slug": "test_wagtail_project",
        "author_name": "Test Author",
        "email": "somebody@example.com",
        "description": "A short description of the project.",
        "domain_name": "example.com",
        "version": "0.0.1",
        "timezone": "Africa/Lusaka",
        "wagtail_username": "somebody",
    }


SUPPORTED_COMBINATIONS = [
    {"python_version": "3.6"},
    {"python_version": "3.7"},
    {"python_version": "3.8"},
    {"use_bootswatch": "n", "bootswatch_theme": "none"},
    {"use_bootswatch": "y", "bootswatch_theme": "cerulean"},
    {"use_bootswatch": "y", "bootswatch_theme": "cosmo"},
    {"use_bootswatch": "y", "bootswatch_theme": "cyborg"},
    {"use_bootswatch": "y", "bootswatch_theme": "darkly"},
    {"use_bootswatch": "y", "bootswatch_theme": "flatly"},
    {"use_bootswatch": "y", "bootswatch_theme": "journal"},
    {"use_bootswatch": "y", "bootswatch_theme": "litera"},
    {"use_bootswatch": "y", "bootswatch_theme": "lumen"},
    {"use_bootswatch": "y", "bootswatch_theme": "lux"},
    {"use_bootswatch": "y", "bootswatch_theme": "materia"},
    {"use_bootswatch": "y", "bootswatch_theme": "minty"},
    {"use_bootswatch": "y", "bootswatch_theme": "pulse"},
    {"use_bootswatch": "y", "bootswatch_theme": "sandstone"},
    {"use_bootswatch": "y", "bootswatch_theme": "simplex"},
    {"use_bootswatch": "y", "bootswatch_theme": "sketchy"},
    {"use_bootswatch": "y", "bootswatch_theme": "slate"},
    {"use_bootswatch": "y", "bootswatch_theme": "solar"},
    {"use_bootswatch": "y", "bootswatch_theme": "spacelab"},
    {"use_bootswatch": "y", "bootswatch_theme": "superhero"},
    {"use_bootswatch": "y", "bootswatch_theme": "united"},
    {"use_bootswatch": "y", "bootswatch_theme": "yeti"},
]

UNSUPPORTED_COMBINATIONS = [
    {"use_bootswatch": "y", "bootswatch_theme": "none"},
    {"use_bootswatch": "n", "bootswatch_theme": "cerulean"},
    {"use_bootswatch": "n", "bootswatch_theme": "cosmo"},
    {"use_bootswatch": "n", "bootswatch_theme": "cyborg"},
    {"use_bootswatch": "n", "bootswatch_theme": "darkly"},
    {"use_bootswatch": "n", "bootswatch_theme": "flatly"},
    {"use_bootswatch": "n", "bootswatch_theme": "journal"},
    {"use_bootswatch": "n", "bootswatch_theme": "litera"},
    {"use_bootswatch": "n", "bootswatch_theme": "lumen"},
    {"use_bootswatch": "n", "bootswatch_theme": "lux"},
    {"use_bootswatch": "n", "bootswatch_theme": "materia"},
    {"use_bootswatch": "n", "bootswatch_theme": "minty"},
    {"use_bootswatch": "n", "bootswatch_theme": "pulse"},
    {"use_bootswatch": "n", "bootswatch_theme": "sandstone"},
    {"use_bootswatch": "n", "bootswatch_theme": "simplex"},
    {"use_bootswatch": "n", "bootswatch_theme": "sketchy"},
    {"use_bootswatch": "n", "bootswatch_theme": "slate"},
    {"use_bootswatch": "n", "bootswatch_theme": "solar"},
    {"use_bootswatch": "n", "bootswatch_theme": "spacelab"},
    {"use_bootswatch": "n", "bootswatch_theme": "superhero"},
    {"use_bootswatch": "n", "bootswatch_theme": "united"},
    {"use_bootswatch": "n", "bootswatch_theme": "yeti"},
]


def _fixture_id(ctx):
    """Helper to get a user friendly test name from the parametrized context."""
    return "-".join(f"{key}:{value}" for key, value in ctx.items())


def build_files_list(root_dir):
    """Build a list containing absolute paths to the generated files."""
    return [
        os.path.join(dirpath, file_path)
        for dirpath, subdirs, files in os.walk(root_dir)
        for file_path in files
    ]


def check_paths(paths):
    """Method to check all paths have correct substitutions."""
    # Assert that no match is found in any of the files
    for path in paths:
        if is_binary(path):
            continue

        for line in open(path, "r"):
            match = RE_OBJ.search(line)
            msg = "cookiecutter variable not replaced in {}"
            assert match is None, msg.format(path)


@pytest.mark.parametrize("context_override", SUPPORTED_COMBINATIONS, ids=_fixture_id)
def test_project_generation(cookies, context, context_override):
    """Test that project is generated and fully rendered."""
    result = cookies.bake(extra_context={**context, **context_override})
    assert result.exit_code == 0
    assert result.exception is None
    assert result.project.basename == context["project_slug"]
    assert result.project.isdir()

    paths = build_files_list(str(result.project))
    assert paths
    check_paths(paths)


@pytest.mark.parametrize("slug", ["project slug", "Project_Slug"])
def test_invalid_slug(cookies, context, slug):
    """Invalid slug should fail pre-generation hook."""
    context.update({"project_slug": slug})

    result = cookies.bake(extra_context=context)

    assert result.exit_code != 0
    assert isinstance(result.exception, FailedHookException)


@pytest.mark.parametrize("invalid_context", UNSUPPORTED_COMBINATIONS)
def test_error_if_incompatible(cookies, context, invalid_context):
    """It should not generate project an incompatible combination is selected."""
    context.update(invalid_context)
    result = cookies.bake(extra_context=context)

    assert result.exit_code != 0
    assert isinstance(result.exception, FailedHookException)
