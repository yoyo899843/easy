FROM python:3.10-slim

WORKDIR /app

COPY src /app
COPY flag /

RUN pip install --no-cache-dir -r requirements.txt gunicorn \
    && chmod 444 /flag

EXPOSE 80
CMD ["gunicorn", "-b", "0.0.0.0:80", "-w", "1", "--threads", "8", "main:app"]
