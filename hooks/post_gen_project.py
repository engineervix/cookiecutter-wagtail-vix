# -*- coding: utf-8 -*-

"""
A portion of this code was adopted from Django's standard crypto functions and
utilities, specifically:
    https://github.com/django/django/blob/master/django/utils/crypto.py

TODO: - Reorganize the private directories and .env files which do not get added to the repository
"""

import os
import random
import shutil
import string

# Get the root project directory
PROJECT_DIRECTORY = os.path.realpath(os.path.curdir)

# Use the system PRNG if possible
try:
    random = random.SystemRandom()
    using_sysrandom = True
except NotImplementedError:
    using_sysrandom = False


def generate_random_string(length=50):
    """
    Returns a securely generated random string.
    The default length of 12 with the a-z, A-Z, 0-9 character set returns
    a 71-bit value. log_2((26+26+10)^12) =~ 71 bits
    """
    punctuation = string.punctuation.replace('"', "").replace("'", "")
    punctuation = punctuation.replace("\\", "")
    if using_sysrandom:
        return "".join(
            random.choice(string.digits + string.ascii_letters + punctuation)
            for i in range(length)
        )

    print(
        "cookiecutter-wagtail-vix couldn't find a secure pseudo-random number generator on your system."
        " Please change your SECRET_KEY variables in the .env file"
        " manually."
    )
    return "CHANGEME!!"


def set_secret_key(config_file_location):
    # Open file
    with open(config_file_location) as f:
        file_ = f.read()

    # Generate a SECRET_KEY that matches the Django standard
    SECRET_KEY = generate_random_string()

    # Replace "CHANGEME!!!" with SECRET_KEY
    file_ = file_.replace("CHANGEME!!!", SECRET_KEY, 1)

    # Write the results to file
    with open(config_file_location, "w") as f:
        f.write(file_)


def make_secret_key(project_directory):
    """Generates and saves random secret key"""

    example_dev_env_file = os.path.join(project_directory, "#envs/env_dev.example")

    dev_env_file = os.path.join(project_directory, "#envs/.dev.env")
    dev_env_sample = os.path.join(project_directory, "#envs/.dev.env.sample")

    example_prod_env_file = os.path.join(project_directory, "#envs/env_prod.example")

    prod_env_file = os.path.join(project_directory, "#envs/.prod.env")
    prod_env_sample = os.path.join(project_directory, "#envs/.prod.env.sample")

    example_test_env_file = os.path.join(project_directory, "#envs/env_test.example")

    test_env_file = os.path.join(project_directory, "#envs/.test.env")
    test_env_sample = os.path.join(project_directory, "#envs/.test.env.sample")

    # create *.env.sample files which should be part of version control
    shutil.copy(example_dev_env_file, dev_env_sample)
    shutil.copy(example_prod_env_file, prod_env_sample)
    shutil.copy(example_test_env_file, test_env_sample)

    shutil.move(example_dev_env_file, dev_env_file)
    shutil.move(example_prod_env_file, prod_env_file)
    shutil.move(example_test_env_file, test_env_file)

    # .env file
    set_secret_key(dev_env_file)
    set_secret_key(prod_env_file)
    set_secret_key(test_env_file)


def setup_db(config_file_location, environment):
    # Open file
    with open(config_file_location) as f:
        file_ = f.read()

    DEV_DB_URL = "sqlite:///" + os.path.join(PROJECT_DIRECTORY, "db.sqlite3")
    TEST_DB_URL = "sqlite:///" + os.path.join(PROJECT_DIRECTORY, "test_db.sqlite3")

    # Replace "CONFIGUREDB!!!" with Correct DB Configuration
    if environment == "dev":
        file_ = file_.replace("CONFIGUREDB!!!", DEV_DB_URL, 1)
    else:
        file_ = file_.replace("CONFIGUREDB!!!", TEST_DB_URL, 1)

    # Write the results to file
    with open(config_file_location, "w") as f:
        f.write(file_)


def make_db_config(project_directory):
    """DB configuration"""

    dev_env_file = os.path.join(project_directory, "#envs/.dev.env")
    test_env_file = os.path.join(project_directory, "#envs/.test.env")

    # env.example file
    setup_db(dev_env_file, "dev")
    setup_db(test_env_file, "test")


def main():
    # Generates and saves random secret key
    make_secret_key(PROJECT_DIRECTORY)
    # sets up DB (SQLite) configuration for dev and test envs
    make_db_config(PROJECT_DIRECTORY)

    # rename these directories so that they are not included in version control
    envs = os.path.join(PROJECT_DIRECTORY, "#envs/")
    vscode = os.path.join(PROJECT_DIRECTORY, "#vscode/")
    resources = os.path.join(PROJECT_DIRECTORY, "#resources/")
    research = os.path.join(PROJECT_DIRECTORY, "#research/")
    logs = os.path.join(PROJECT_DIRECTORY, "#logs/")
    backups = os.path.join(PROJECT_DIRECTORY, "#backups/")

    # the renamed versions are in the .gitignore file
    shutil.move(envs, os.path.join(PROJECT_DIRECTORY, ".envs/"))
    shutil.move(vscode, os.path.join(PROJECT_DIRECTORY, ".vscode/"))
    shutil.move(resources, os.path.join(PROJECT_DIRECTORY, ".resources/"))
    shutil.move(research, os.path.join(PROJECT_DIRECTORY, ".research/"))
    shutil.move(logs, os.path.join(PROJECT_DIRECTORY, ".logs/"))
    shutil.move(backups, os.path.join(PROJECT_DIRECTORY, ".backups/"))

    print(
        "Please ensure that you use {{ cookiecutter.wagtail_user_email }} as your email address when you run `./manage.py createsuperuser`"
    )


if __name__ == "__main__":
    main()
