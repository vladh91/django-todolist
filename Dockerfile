FROM python:3.5-alpine

RUN pip install django

ADD . /
ENTRYPOINT ["python3.5","manage.py runserver"]