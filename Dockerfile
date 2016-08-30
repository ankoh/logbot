FROM python:3
MAINTAINER André Kohn <andre@kohn.io>

# Install python dependencies cache-friendly
COPY Makefile requirements.txt /opt/logbot/
RUN cd /opt/logbot && make install

# Set PYTHONPATH
ENV PYTHONPATH /opt/logbot:$PYTHONPATH

# Copy sources
COPY bot /opt/logbot/bot/
COPY sql /opt/logbot/sql/
COPY runner.py entrypoint.sh /opt/logbot/
RUN chmod +x /opt/logbot/entrypoint.sh

# Prepare entrypoint
ENTRYPOINT ["/opt/logbot/entrypoint.sh"]
CMD ["python", "/opt/logbot/runner.py"]
