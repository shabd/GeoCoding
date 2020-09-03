FROM python:3.8-alpine
LABEL Assessment Task

ENV PYTHONBUFFERED 1

COPY ./requirements.txt /requirements.txt
RUN pip install -r /requirements.txt

