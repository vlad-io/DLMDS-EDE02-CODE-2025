FROM postgres:latest

ENV POSTGRES_PASSWORD=password
ENV POSTGRES_USER=appuser
ENV POSTGRES_DB=mydatabase

# COPY init.sql /docker-entrypoint-initdb.d/