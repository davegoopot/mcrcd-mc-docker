#!/bin/bash

sudo docker build -t local:flask_latest flaskserver

CONTAINER=$(sudo docker run -p 8888:5000 -d local:flask-latest)

sudo docker log $CONTAINER
