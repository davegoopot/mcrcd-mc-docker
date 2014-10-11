#!/bin/bash

## Expecting to be used as ./snapshot.bash NAME
## Tags the two running servers as
##  local/mc:NAME
##  local/web:NAME

die () {
    echo >&2 "$@"
    exit 1
}

[ "$#" -eq 1 ] || die "1 argument required, $# provided"

sudo docker commit mc local/mc:$1
sudo docker commit web local/web:$1
