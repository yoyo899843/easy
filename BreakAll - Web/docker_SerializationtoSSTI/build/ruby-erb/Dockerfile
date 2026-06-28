FROM ubuntu

RUN apt-get update
RUN apt-get install -y ruby
RUN apt-get install -y nmap
RUN gem install sinatra

RUN adduser --disabled-password --gecos '' lab2
COPY lab2/ /home/lab2

RUN chmod +x /home/lab2/main.rb
RUN chmod +x /home/lab2/run.sh

RUN chown -R root:lab2 /home/lab2/
RUN chmod 750 /home/lab2
RUN chmod 740 /usr/bin/top
RUN chmod 740 /bin/ps
RUN chmod 740 /usr/bin/pgrep
RUN export TERM=xterm

WORKDIR /home/lab2/

EXPOSE 11111
CMD su lab2 -c "ruby /home/lab2/main.rb"
