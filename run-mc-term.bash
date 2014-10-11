#!/bin/bash

die () {
    echo >&2 "$@"
    exit 1
}

[ "$#" -eq 1 ] || die "1 argument required, $# provided"

sudo docker rm -f mc

sudo docker run -ti -p 25565:25565 -p 4711:4711 --name mc $1 /bin/bash

