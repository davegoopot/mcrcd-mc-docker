#!/bin/bash

sudo docker rm -f web

sudo docker run -d -p 8888:5000  --name web --link mc:mc davegoopot/mcrcd:web_latest 
