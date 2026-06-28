FROM python:2.7
MAINTAINER RB363

RUN apt-get update -y

COPY method.py .
# COPY method.html .
COPY requirements.txt .

RUN pip install -r requirements.txt

ENTRYPOINT ["python"]
CMD ["method.py"]
