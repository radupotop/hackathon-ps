FROM python:3.8.0-slim

COPY . /opt/app
WORKDIR /opt/app
RUN pip install --no-cache-dir -r requirements.txt && \
    pip install --no-cache-dir -e .
EXPOSE 5000
CMD python app/api.py
