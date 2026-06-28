FROM python:3.12-alpine
WORKDIR /app
RUN pip install flask docker --no-cache-dir
COPY . .
CMD ["python", "app.py"]
