FROM davegoopot/mcrcd:mcserver
MAINTAINER dave@goopot.co.uk

EXPOSE 25565

copy server.properties /bukkit/
copy ops.json /bukkit/
COPY world/ /bukkit/world/

WORKDIR /bukkit


