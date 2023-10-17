FROM --platform=linux/amd64 python:3.8-slim

ENV CELERY_CONF_PATH=celeryconfig

WORKDIR /app
COPY . .
RUN pip install -r requirements.txt