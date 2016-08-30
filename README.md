[![build status](https://gitlab.kohn.io/ankoh/logbot/badges/master/build.svg)](https://gitlab.kohn.io/ankoh/logbot/commits/master) [![coverage report](https://gitlab.kohn.io/ankoh/logbot/badges/master/coverage.svg)](https://gitlab.kohn.io/ankoh/logbot/commits/master)

# Logbot
**`Logbot` is a tiny Python Slack bot that uses the Slack RTM API to log channel conversations and write them into a Postgres
database.**

Right now, only simple messages are processed but it's quite easy to add support for a wider range of events.

More information on the Slack RTM API: https://api.slack.com/rtm

## Usage

```
# Prerequisites:
# * Create a bot in the slack team settings
# * Copy the bot api key into the compose file
# * BE_CREATIVE otherwise the value will default to the yml's folder name

BE_CREATIVE=myfancylogbot

# Create logbot
docker-compose -f compose.yml -p $BE_CREATIVE up -d

# Watch the bot botting
docker-compose -f compose.yml -p $BE_CREATIVE logs -f bot

# Connect to the database (use password of compose file)
docker exec -it $(BE_CREATIVE)_data_1 psql --dbname logbot_db --user logbot_runner --password

# Start the bot
docker-compose -f compose.yml -p $BE_CREATIVE start

# Stop the bot
docker-compose -f compose.yml -p $BE_CREATIVE stop

# Delete the bot INCLUDING its data
docker-compose -f compose.yml -p $BE_CREATIVE rm -vf

# Update the bot PRESERVING the data
# Schema changes require some work with table altering!
docker pull ankoh/logbot:latest
docker-compose -f compose.yml -p $BE_CREATIVE up -d bot
```

## Development
```
# Files:
# /bot/rtm.py             RTM API Client
# /bot/pg.py              Postgres Client
# /bot/ctrl.py            Bot Controller
# /sql/create_schema.sql  Postgres Schema

# Targets
make install         # Install pip dependencies
make freeze          # Freeze pip dependencies
make image           # Build docker image
make tests           # Run tests
make coverage        # Run coverage
```
