FROM ubuntu:16.04

RUN apt-get update && apt-get upgrade -y
RUN apt-get install -y build-essential socat

RUN adduser --disabled-password --gecos '' lab5
COPY lab5/ /home/lab5
RUN chmod +x /home/lab5/plt
RUN chown -R root:lab5 /home/lab5/
RUN chmod 750 /home/lab5
RUN touch /home/lab5/flag
RUN chown root:lab5 /home/lab5/flag
RUN chmod 440 /home/lab5/flag
RUN chmod 740 /usr/bin/top
RUN chmod 740 /bin/ps
RUN chmod 740 /usr/bin/pgrep
RUN export TERM=xterm

WORKDIR /home/lab5/


EXPOSE 2120
CMD su lab5 -c "socat TCP-LISTEN:2120,reuseaddr,fork EXEC:/home/lab5/plt"
