#################################################################################
# use node:18.19-bookworm as the base image for building the frontend
#################################################################################

FROM node:18.19-bookworm as frontend-builder

# A wildcard is used to ensure both package.json AND package-lock.json are copied
# where available (npm@5+)
COPY package*.json .babelrc.js webpack.config.js ./
RUN npm ci --no-optional --no-audit --progress=false --network=host

COPY ./{{cookiecutter.project_slug}}/assets ./{{cookiecutter.project_slug}}/assets
RUN npm run build:prod

#################################################################################
# use python:3.12-slim-bookworm as the base image for production and development
#################################################################################

FROM python:3.12-slim-bookworm as production

# Add user that will be used in the container
RUN groupadd wagtail && \
    useradd --create-home --shell /bin/bash -g wagtail wagtail

RUN mkdir -p /home/wagtail/app && chown wagtail:wagtail /home/wagtail/app

# set work directory
WORKDIR /home/wagtail/app

# Port used by this container to serve HTTP.
EXPOSE 8000

# set environment variables
# 1. Force Python stdout and stderr streams to be unbuffered.
# 2. Set PORT variable that is used by Gunicorn. This should match "EXPOSE"
#    command.
ENV PYTHONUNBUFFERED=1 \
    PYTHONHASHSEED=random \
    PYTHONPATH=/home/wagtail/app \
    DJANGO_SETTINGS_MODULE={{cookiecutter.project_slug}}.settings.production \
    ## Note: feel free to adjust WEB_CONCURRENCY based on the memory requirements of your processes
    ## ref: https://docs.gunicorn.org/en/stable/settings.html
    ## The suggested number of workers is (2*CPU)+1
    WEB_CONCURRENCY=3 \
    NODE_MAJOR=18

# Install system dependencies required by Wagtail, Django and the project
RUN apt-get update --yes --quiet && apt-get install --yes --quiet --no-install-recommends \
    build-essential \
    ca-certificates gnupg \
    curl \
    gdal-bin libgdal-dev binutils libproj-dev \
    git \
    imagemagick \
    libjpeg62-turbo-dev \
    libmagic1 \
    libpq-dev \
    libwebp-dev \
    zlib1g-dev \
    && apt-get clean

# Install node (Keep the version in sync with the node container above)
RUN mkdir -p /etc/apt/keyrings
RUN curl -fsSL https://deb.nodesource.com/gpgkey/nodesource-repo.gpg.key | gpg --dearmor -o /etc/apt/keyrings/nodesource.gpg
RUN echo "deb [signed-by=/etc/apt/keyrings/nodesource.gpg] https://deb.nodesource.com/node_${NODE_MAJOR}.x nodistro main" | tee /etc/apt/sources.list.d/nodesource.list
RUN apt-get update
RUN apt install nodejs -y

# Use user "wagtail" to run the build commands below and the server itself.
USER wagtail

# set up virtual environment & install python dependencies
ARG DEVELOPMENT
ARG POETRY_VERSION=1.6.1
ENV VIRTUAL_ENV=/home/wagtail/venv \
    DEVELOPMENT=${DEVELOPMENT}
RUN python -m venv $VIRTUAL_ENV
ENV PATH="$VIRTUAL_ENV/bin:$PATH"
RUN pip install --upgrade pip
RUN python -m pip install poetry==$POETRY_VERSION

COPY --chown=wagtail ./pyproject.toml .
COPY --chown=wagtail ./poetry.lock .
RUN poetry install ${DEVELOPMENT:+--with dev,test,docs} --no-root

# install mjml
# NOTE: the version must match the one in package.json
RUN npm install -D mjml@"^4.14.1"

# Copy build artifacts from frontend-builder stage
RUN mkdir -p /home/wagtail/app/{{cookiecutter.project_slug}}/static
COPY --from=frontend-builder --chown=wagtail:wagtail /{{cookiecutter.project_slug}}/static /home/wagtail/app/{{cookiecutter.project_slug}}/static

# Copy the source code of the project into the container
COPY --chown=wagtail:wagtail . .

# Run poetry install again to install the project (so that the `{{cookiecutter.project_slug}}` package is always importable)
RUN poetry install

# Run collectstatic.
# This step is deferred, because it somehow messes up production settings
# RUN python manage.py collectstatic --noinput --clear

# Runtime command that executes when "docker run" is called
CMD gunicorn {{cookiecutter.project_slug}}.wsgi:application

#################################################################################
# The next steps won't be run in production
#################################################################################

FROM production as dev

# Swap user, so the following tasks can be run as root
USER root

# Install `psql`, useful for `manage.py dbshell`
RUN apt-get install -y postgresql-client

# Restore user
USER wagtail

# Pull in the node modules for the frontend
COPY --chown=wagtail:wagtail --from=frontend-builder ./node_modules ./node_modules

# do nothing - exec commands elsewhere
CMD tail -f /dev/null
