#!/bin/bash

sudo docker commit --author="dave@goopot.co.uk" --message="Pushing updates for coderdojo" web davegoopot/mcrcd:web-sep2014
sudo docker commit --author="dave@goopot.co.uk" --message="Pushing updates for coderdojo" mc davegoopot/mcrcd:mc-sep2014

sudo docker push davegoopot/mcrcd:web-sep2014
sudo docker push davegoopot/mcrcd:mc-sep2014 1