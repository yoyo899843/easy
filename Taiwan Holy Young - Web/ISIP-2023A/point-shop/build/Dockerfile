FROM python:3.10-slim

WORKDIR /app

COPY app /app

RUN pip install --no-cache-dir Flask==2.2.2 Werkzeug==2.2.2 gunicorn

EXPOSE 80
CMD ["gunicorn", "-b", "0.0.0.0:80", "-w", "1", "--threads", "8", "main:app"]
