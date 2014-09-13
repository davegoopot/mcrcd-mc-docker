#!/bin/bash

sudo docker rm -f web
sudo docker rm -f mc

./build-images.bash

sudo docker run -d -p 25565:25565 -p 4711:4711 --name mc local:mc_latest java -jar craftbukkit-beta.jar --noconsole 
sudo docker run -d -p 8888:5000  --name web --link mc:mc local:flask_latest
