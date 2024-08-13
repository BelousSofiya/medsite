FROM python:3.9-alpine

RUN mkdir -p /home/medsite

RUN addgroup -S medsite && adduser -S medsite -G medsite

ENV HOME=/home/medsite
ENV APP_HOME=/home/medsite/app
RUN mkdir $APP_HOME

WORKDIR $APP_HOME

ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

RUN apk update \
    && apk add postgresql-dev gcc python3-dev musl-dev

RUN pip install --upgrade pip
COPY ./requirements.txt .
RUN pip3 install -r requirements.txt

COPY . $APP_HOME

RUN chown -R medsite:medsite $APP_HOME

USER medsite