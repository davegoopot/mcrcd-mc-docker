#!/bin/bash

sudo docker build -t :flask-latest flaskserver

CONTAINER=$(sudo docker run -p 8888:5000 -d :flask-latest)

sudo docker log $CONTAINER
