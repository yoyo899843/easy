FROM ubuntu:18.04

WORKDIR /root

RUN echo 'debconf debconf/frontend select Noninteractive' | debconf-set-selections
RUN apt-get update && \
    apt-get install -y \
    curl git build-essential python python3 libffi-dev libssl-dev python-mpmath python3-pip socat \
    zlib1g-dev libffi-dev libbz2-dev libreadline-dev sqlite3 libsqlite3-dev libssl-dev libncurses5 libncurses5-dev libncursesw5

RUN pip3 install pycryptodome

COPY share/ /home/ctf/
RUN chmod +x /home/ctf/run.sh /home/ctf/server.py

CMD socat TCP-LISTEN:9999,reuseaddr,fork EXEC:/home/ctf/run.sh
