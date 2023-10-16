FROM --platform=linux/amd64 python:3.8-slim

WORKDIR /app
COPY . .
RUN pip install -r requirements.txt