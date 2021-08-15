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
        "github_username": "engineervix",
        "email": "somebody@example.com",
        "description": "A short description of the project.",
        "domain_name": "example.com",
        "version": "0.0.1",
        "timezone": "Africa/Lusaka",
        "wagtail_user_email": "somebody@example.com",
    }


SUPPORTED_COMBINATIONS = [
    {"python_version": "3.6"},
    {"python_version": "3.7"},
    {"python_version": "3.8"},
    {"python_version": "3.9"},
]

# UNSUPPORTED_COMBINATIONS = [
#     {"use_bootswatch": "y", "bootswatch_theme": "none"},
#     {"use_bootswatch": "n", "bootswatch_theme": "cerulean"},
# ]


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


# @pytest.mark.parametrize("invalid_context", UNSUPPORTED_COMBINATIONS)
# def test_error_if_incompatible(cookies, context, invalid_context):
#     """It should not generate project if an incompatible combination is selected."""
#     context.update(invalid_context)
#     result = cookies.bake(extra_context=context)

#     assert result.exit_code != 0
#     assert isinstance(result.exception, FailedHookException)
