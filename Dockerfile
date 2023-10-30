FROM python:3.11

WORKDIR /app

COPY . .

COPY requirements.txt requirements.txt

RUN pip install -r requirements.txt

