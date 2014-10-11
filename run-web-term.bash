#!/bin/bash

die () {
    echo >&2 "$@"
    exit 1
}

[ "$#" -eq 1 ] || die "1 argument required, $# provided"

sudo docker rm -f web

sudo docker run -ti -p 8888:5000  --name web --link mc:mc $1 /bin/bash
