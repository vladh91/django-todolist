FROM python:3.5-alpine

ADD . /
ENTRYPOINT ["python","manage.py runserver"]