#!/bin/bash

sudo docker rm -f mc

sudo docker run -d -p 25565:25565 -p 4711:4711 --name mc local:mc_latest java -jar craftbukkit-beta.jar --noconsole 

