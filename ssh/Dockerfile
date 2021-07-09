FROM ubuntu:20.04

RUN apt update && apt install -y locales tree ssh nano vim htop && rm -rf /var/lib/apt/lists/* \
    && localedef -i en_US -c -f UTF-8 -A /usr/share/locale/locale.alias en_US.UTF-8

ENV LANG en_US.utf8

RUN mkdir ~/.ssh && touch ~/.ssh/authorized_keys \ 
    && chmod -u=rwX,go= ~/.ssh && chmod -u=rw,go=r ~/.ssh/authorized_keys

ADD sshd_config /etc/ssh/sshd_config 


ADD entrypoint.sh .
RUN chmod 700 entrypoint.sh

ENTRYPOINT ["sh", "entrypoint.sh"]