FROM ubuntu

RUN apt-get update
RUN apt-get install -y ruby
RUN apt-get install -y nmap

RUN adduser --disabled-password --gecos '' lab1
COPY lab1/ /home/lab1

RUN chmod +x /home/lab1/baby.rb
RUN chmod +x /home/lab1/run.sh

RUN chown -R root:lab1 /home/lab1/
RUN chmod 750 /home/lab1
RUN chmod 740 /usr/bin/top
RUN chmod 740 /bin/ps
RUN chmod 740 /usr/bin/pgrep
RUN export TERM=xterm

WORKDIR /home/lab1/

EXPOSE 5278
CMD su lab1 -c "ncat -vc 'ruby /home/lab1/baby.rb' -kl 5278"







