FROM davegoopot/mcrcd:mcserver
MAINTAINER dave@goopot.co.uk

EXPOSE 25565

COPY worlds/level.dat /bukkit/world/
COPY worlds/server.properties /bukkit/

WORKDIR /bukkit

CMD java -jar craftbukkit-beta.jar --noconsole 


