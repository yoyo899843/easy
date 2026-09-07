FROM python:3.10-slim

WORKDIR /app

COPY level1 /app

RUN pip install --no-cache-dir Flask==2.2.2 Werkzeug==2.2.2 gunicorn \
    && chmod 444 /app/flag

EXPOSE 80
CMD ["gunicorn", "-b", "0.0.0.0:80", "-w", "1", "--threads", "8", "main:app"]
