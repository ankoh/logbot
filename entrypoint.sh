#!/bin/sh

DIR=/opt/logbot
INIT=$DIR/init

if [ ! -f $INIT ]; then
   python $DIR/runner.py -t prepare
   touch $INIT
fi

exec "$@"
