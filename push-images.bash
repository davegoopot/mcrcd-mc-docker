#!/bin/bash

sudo docker commit --author="dave@goopot.co.uk" --message="Pushing updates for coderdojo" web davegoopot/mcrcd:web_latest
sudo docker commit --author="dave@goopot.co.uk" --message="Pushing updates for coderdojo" mc davegoopot/mcrcd:mc_latest

sudo docker push davegoopot/mcrcd:web_latest
sudo docker push davegoopot/mcrcd:mc_latest