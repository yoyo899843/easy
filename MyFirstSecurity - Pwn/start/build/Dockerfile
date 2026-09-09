FROM --platform=linux/amd64 debian:bullseye-slim

RUN printf 'Acquire::Check-Valid-Until "false";\n' > /etc/apt/apt.conf.d/99no-check-valid-until \
    && apt-get update \
    && apt-get install -y --no-install-recommends socat \
    && rm -rf /var/lib/apt/lists/* \
    && useradd -m ctf

COPY start /home/ctf/start
COPY flag /home/ctf/flag
RUN chmod 555 /home/ctf/start && chmod 444 /home/ctf/flag

WORKDIR /home/ctf
EXPOSE 9999
CMD ["socat", "TCP-LISTEN:9999,reuseaddr,fork", "EXEC:/home/ctf/start,su=ctf"]
