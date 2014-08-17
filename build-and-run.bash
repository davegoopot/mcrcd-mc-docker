#!/bin/bash

IMAGE=$(sudo docker build flaskserver)

CONTAINER=$(sudo docker run -p 8888:5000 -d $IMAGE)

sudo docker log $CONTAINER
