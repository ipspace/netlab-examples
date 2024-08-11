FROM ubuntu:22.04
ENV DEBIAN_FRONTEND=noninteractive

LABEL maintainer="Netlab project <netlab.tools>"
LABEL description="bgpipe container"

RUN apt-get update && \
  apt-get install -y bash iputils-ping net-tools iproute2 wget jq && \
  wget https://github.com/bgpfix/bgpipe/releases/download/v0.8.8/bgpipe-linux-amd64 -q -O /usr/local/bin/bgpipe && \
  chmod a+x /usr/local/bin/bgpipe

WORKDIR /root

CMD /usr/bin/bash
