FROM python:3.8.0-slim

RUN apt-get update && apt-get -y install file libmagic1

COPY . /opt/app
WORKDIR /opt/app

RUN pip install --no-cache-dir -r requirements.txt && \
    pip install --no-cache-dir -e .
CMD python app/api.py

EXPOSE 5000
