#!/bin/bash

sudo docker rm -f web
sudo docker rm -f mc

sudo docker build -t local:mc_latest mcserver
sudo docker build -t local:flask_latest flaskserver

sudo docker run -d -p 25565:25565 -p 4711:4711 --name mc local:mc_latest
sudo docker run -d -p 8888:5000  --name web --link mc:mc local:flask_latest
