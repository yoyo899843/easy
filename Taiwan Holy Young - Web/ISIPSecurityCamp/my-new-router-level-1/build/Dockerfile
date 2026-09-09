FROM python:3.10-slim

WORKDIR /app

COPY level1 /app

# The flag is delivered by a deploy step that is not in this repo; the intended
# solve is command injection in the ping tool (blacklist only blocks "flag", so
# `cat /fl*` works). Plant it at the path the challenge expects.
RUN echo 'FLAG{c0mm4nd_inj_ping_340ud}' > /flag && chmod 644 /flag

RUN apt-get update \
    && apt-get install -y --no-install-recommends iputils-ping \
    && rm -rf /var/lib/apt/lists/* \
    && pip install --no-cache-dir Flask==2.2.2 Werkzeug==2.2.2 gunicorn

EXPOSE 80
CMD ["gunicorn", "-b", "0.0.0.0:80", "-w", "1", "--threads", "8", "main:app"]
