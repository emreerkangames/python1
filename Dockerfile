FROM python:3.11-slim

ENV PYTHONDONTWRITEBYTECODE=1
ENV PYTHONUNBUFFERED=1

WORKDIR /code

COPY requirements.txt /code/
RUN apt-get update && apt-get install -y gcc python3-dev && pip install --no-cache-dir -r requirements.txt


COPY . /code/