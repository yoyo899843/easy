FROM ubuntu:16.04

RUN apt-get update && apt-get upgrade -y
RUN apt-get install -y build-essential socat

RUN adduser --disabled-password --gecos '' lab2
COPY lab2/ /home/lab2
RUN chmod +x /home/lab2/binary
RUN chown -R root:lab2 /home/lab2/
RUN chmod 750 /home/lab2
RUN touch /home/lab2/flag
RUN chown root:lab2 /home/lab2/flag
RUN chmod 440 /home/lab2/flag
RUN chmod 740 /usr/bin/top
RUN chmod 740 /bin/ps
RUN chmod 740 /usr/bin/pgrep
RUN export TERM=xterm

WORKDIR /home/lab2/


EXPOSE 2117
CMD su lab2 -c "socat TCP-LISTEN:2117,reuseaddr,fork EXEC:/home/lab2/binary"
