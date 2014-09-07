#!/bin/bash

sudo docker build -t local:flask_latest flaskserver

CONTAINER=$(sudo docker run -p 8888:5000 -d local:flask_latest)

echo I built this container: $CONTAINER
