FROM python:3.5-alpine

ENV PYTHONUNBUFFERED 1

RUN pip install django
RUN apt install -y python-mysqldb


ADD . /usr/local/app
WORKDIR /usr/local/app

EXPOSE 8000
ENTRYPOINT ["python3.5", "manage.py", "runserver"]