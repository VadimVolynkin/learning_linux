FROM ubuntu:20.04

ENV DEBIAN_FRONTEND noninteractive
RUN apt-get update && apt-get install -y ubuntu-server locales tree ssh && rm -rf /var/lib/apt/lists/* \
    && localedef -i en_US -c -f UTF-8 -A /usr/share/locale/locale.alias en_US.UTF-8

ADD sshd_config /etc/ssh/sshd_config

ADD entrypoint.sh .
RUN chmod 700 entrypoint.sh

ENTRYPOINT [ "sh", "entrypoint.sh" ]