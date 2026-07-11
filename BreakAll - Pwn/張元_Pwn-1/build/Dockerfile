FROM ubuntu:14.04

RUN apt-get update && apt-get upgrade -y
RUN apt-get install -y build-essential socat

RUN adduser --disabled-password --gecos '' lab1
COPY lab1/ /home/lab1
RUN chmod +x /home/lab1/luck
RUN chown -R root:lab1 /home/lab1/
RUN chmod 750 /home/lab1
RUN touch /home/lab1/flag.txt
RUN chown root:lab1 /home/lab1/flag.txt
RUN chmod 440 /home/lab1/flag.txt
RUN chmod 740 /usr/bin/top
RUN chmod 740 /bin/ps
RUN chmod 740 /usr/bin/pgrep
RUN export TERM=xterm

WORKDIR /home/lab1/


EXPOSE 2111
CMD su lab1 -c "socat TCP-LISTEN:2111,reuseaddr,fork EXEC:/home/lab1/luck"
