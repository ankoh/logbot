FROM python:3
MAINTAINER André Kohn <andre@kohn.io>

# Install python dependencies cache-friendly
COPY Makefile requirements.txt /opt/logbot/
RUN cd /opt/logbot && make install

# Copy sources
COPY bot sql/schema.sql docker/entrypoint.sh /opt/logbot/
