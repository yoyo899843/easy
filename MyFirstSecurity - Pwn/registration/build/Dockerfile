FROM --platform=linux/amd64 debian:bullseye-slim

# bullseye is old enough to still provide the compat `gets` symbol this binary
# imports (removed in glibc >= 2.34). The valid-until override keeps apt working
# regardless of the build host's clock.
RUN printf 'Acquire::Check-Valid-Until "false";\n' > /etc/apt/apt.conf.d/99no-check-valid-until \
    && apt-get update \
    && apt-get install -y --no-install-recommends socat \
    && rm -rf /var/lib/apt/lists/* \
    && useradd -m ctf

COPY registration /home/ctf/registration
COPY flag /home/ctf/flag
RUN chmod 555 /home/ctf/registration && chmod 444 /home/ctf/flag

WORKDIR /home/ctf
EXPOSE 9999
CMD ["socat", "TCP-LISTEN:9999,reuseaddr,fork", "EXEC:/home/ctf/registration,su=ctf"]
