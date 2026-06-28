FROM ubuntu:18.04
RUN apt-get update && apt-get install -y xinetd
RUN useradd -m baby_ghost
RUN chmod 774 /tmp
RUN chmod 1733 /tmp /var/tmp /dev/shm
RUN chown -R root:root /home/baby_ghost
CMD ["/usr/sbin/xinetd", "-dontfork"]
