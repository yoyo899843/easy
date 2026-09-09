FROM --platform=linux/amd64 debian:bullseye-slim

RUN printf 'Acquire::Check-Valid-Until "false";\n' > /etc/apt/apt.conf.d/99no-check-valid-until \
    && apt-get update \
    && apt-get install -y --no-install-recommends socat \
    && rm -rf /var/lib/apt/lists/* \
    && useradd -m lab2

COPY lab2/binary /home/lab2/binary
COPY lab2/flag /home/lab2/flag
RUN chmod 555 /home/lab2/binary \
    && chown root:lab2 /home/lab2/flag \
    && chmod 440 /home/lab2/flag

WORKDIR /home/lab2
EXPOSE 2117
CMD ["socat", "TCP-LISTEN:2117,reuseaddr,fork", "EXEC:/home/lab2/binary,su=lab2"]
