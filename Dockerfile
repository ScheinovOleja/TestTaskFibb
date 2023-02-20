FROM python:3.10

RUN pip install pika

WORKDIR .
COPY app.py .

CMD ["python", "app.py"]