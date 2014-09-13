#!/bin/bash


sudo docker build -t local:mc_latest mcserver
sudo docker build -t local:flask_latest flaskserver