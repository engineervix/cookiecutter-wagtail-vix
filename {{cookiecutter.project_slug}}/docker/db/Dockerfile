# pull official base image
FROM postgis/postgis:15-3.4

# run create.sql on init
ADD create.sql /docker-entrypoint-initdb.d/
