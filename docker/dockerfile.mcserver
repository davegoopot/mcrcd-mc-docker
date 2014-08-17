FROM davegoopot/mcrcd:mcserver
MAINTAINER dave@goopot.co.uk

EXPOSE 25655

COPY ../worlds/level.dat /bukkit/world

WORKDIR /bukkit

CMD ["/bin/bash", "java -jar craftbukkit-beta.jar --noconsole"] 


