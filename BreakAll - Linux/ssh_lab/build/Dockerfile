FROM ubuntu:16.04

RUN dpkg --add-architecture i386

RUN apt-get update && apt-get upgrade -y
RUN apt-get install -y libc6-dbg libc6-dbg:i386 lib32stdc++6
RUN apt-get install -y curl git zip unzip vim nano binutils
RUN apt-get install -y socat net-tools netcat nmap apache2
RUN apt-get install -y openssh-server

RUN mkdir /var/run/sshd

RUN echo 'root:myfirstpassword' |chpasswd

RUN sed -ri 's/^PermitRootLogin\s+.*/PermitRootLogin yes/' /etc/ssh/sshd_config
RUN sed -ri 's/UsePAM yes/#UsePAM yes/g' /etc/ssh/sshd_config
RUN sed -ri 's/^#MaxStartups\s+.*/MaxStartups 1000/' /etc/ssh/sshd_config
RUN sed -i '$a ClientAliveInterval 1' /etc/ssh/sshd_config

RUN chmod 740 /usr/bin/passwd


RUN adduser --disabled-password --gecos '' lab
RUN echo 'lab:Ksu@lab' |chpasswd
RUN chown root.root /home/lab/.bashrc

COPY lab/flag /home/lab
COPY lab/.hidden /home/lab
COPY lab/base64.txt /home/lab
COPY lab/hex.txt /home/lab
COPY lab/secret /opt/

COPY lab/bin/flag /bin/
RUN chmod +x /bin/flag
COPY lab/start.sh /bin/
RUN chmod +x /bin/start.sh


COPY lab/index.html /var/www/html/
RUN chown root.root /home/lab/

CMD ["/usr/sbin/sshd", "-D"]

EXPOSE 22

