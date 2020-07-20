FROM python:3.8-slim

RUN apt-get update && apt-get install -y build-essential

WORKDIR /usr/src/app

COPY ./requirements.txt ./requirements.txt

RUN pip install -r requirements.txt
