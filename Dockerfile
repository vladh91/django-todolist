FROM python:3.5-alpine

ENV PYTHONUNBUFFERED 1

RUN pip install django
RUN pip install mysql-connector


ADD . /usr/local/app
WORKDIR /usr/local/app
ENTRYPOINT ["python3.5","manage.py runserver"]