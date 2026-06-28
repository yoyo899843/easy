FROM ubuntu:16.04

RUN apt-get update && apt-get upgrade -y
RUN apt-get install -y build-essential socat

RUN adduser --disabled-password --gecos '' lab4
COPY lab4/ /home/lab4
RUN chmod +x /home/lab4/shellcode
RUN chown -R root:lab4 /home/lab4/
RUN chmod 750 /home/lab4
RUN touch /home/lab4/flag
RUN chown root:lab4 /home/lab4/flag
RUN chmod 440 /home/lab4/flag
RUN chmod 740 /usr/bin/top
RUN chmod 740 /bin/ps
RUN chmod 740 /usr/bin/pgrep
RUN export TERM=xterm

WORKDIR /home/lab4/


EXPOSE 2119
CMD su lab4 -c "socat TCP-LISTEN:2119,reuseaddr,fork EXEC:/home/lab4/shellcode"
