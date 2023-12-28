import os
import secrets
import shutil

# Get the root project directory
PROJECT_DIRECTORY = os.path.realpath(os.path.curdir)


def generate_secret_key(config_file_location):
    # Open file
    with open(config_file_location) as f:
        file_ = f.read()

    # Generate a SECRET_KEY
    SECRET_KEY = secrets.token_hex(25)

    file_ = file_.replace(
        "DJANGO_SECRET_KEY=secret",
        f"DJANGO_SECRET_KEY={SECRET_KEY}",
    )

    # Write the results to file
    with open(config_file_location, "w") as f:
        f.write(file_)


def set_secret_key(project_directory):
    example_dotenv_file = os.path.join(project_directory, ".env.sample")
    dotenv_file = os.path.join(project_directory, ".env")

    shutil.copy(example_dotenv_file, dotenv_file)

    generate_secret_key(dotenv_file)


def main():
    # Generate and set random secret key
    set_secret_key(PROJECT_DIRECTORY)

    # rename directory so that it's not included in version control
    vscode = os.path.join(PROJECT_DIRECTORY, "#vscode/")

    # the renamed version is in the .gitignore file
    shutil.move(vscode, os.path.join(PROJECT_DIRECTORY, ".vscode/"))


if __name__ == "__main__":
    main()
