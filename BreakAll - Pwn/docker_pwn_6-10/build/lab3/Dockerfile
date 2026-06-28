FROM ubuntu:16.04

RUN apt-get update && apt-get upgrade -y
RUN apt-get install -y build-essential socat

RUN adduser --disabled-password --gecos '' lab3
COPY lab3/ /home/lab3
RUN chmod +x /home/lab3/return
RUN chown -R root:lab3 /home/lab3/
RUN chmod 750 /home/lab3
RUN touch /home/lab3/flag
RUN chown root:lab3 /home/lab3/flag
RUN chmod 440 /home/lab3/flag
RUN chmod 740 /usr/bin/top
RUN chmod 740 /bin/ps
RUN chmod 740 /usr/bin/pgrep
RUN export TERM=xterm

WORKDIR /home/lab3/


EXPOSE 2118
CMD su lab3 -c "socat TCP4-LISTEN:2118,fork EXEC:/home/lab3/return"
