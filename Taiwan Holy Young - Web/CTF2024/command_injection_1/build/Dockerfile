FROM tiangolo/uwsgi-nginx-flask:python3.10

COPY src /app
RUN chmod 444 /app/flag
RUN apt-get update -y
RUN apt-get install -y iputils-ping
RUN pip3 install -r requirements.txt

CMD python3 main.py