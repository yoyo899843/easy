FROM python:3.10-slim

WORKDIR /home/ctf

RUN apt-get update \
    && apt-get install -y --no-install-recommends socat \
    && rm -rf /var/lib/apt/lists/* \
    && pip install --no-cache-dir pycryptodome

COPY share/ /home/ctf/
RUN chmod +x /home/ctf/run.sh /home/ctf/server.py

CMD socat TCP-LISTEN:9999,reuseaddr,fork EXEC:/home/ctf/run.sh
