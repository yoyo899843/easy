FROM ubuntu:16.04
MAINTAINER frozenkp <csjh21010@gmail.com>
RUN useradd -m ctf
RUN chmod 774 /tmp
RUN chmod -R 774 /var/tmp
RUN chmod -R 774 /dev
RUN chmod -R 774 /run
RUN chmod 1733 /tmp /var/tmp /dev/shm
RUN chown -R root:root /home/ctf
CMD ["/home/ctf/service", "-c", "/home/ctf/service.yaml"]
