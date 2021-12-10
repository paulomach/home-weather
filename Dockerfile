FROM python:3.9-alpine

ENV PYTHONUNBUFFERED 1

COPY runtime-requirements.txt /app
RUN pip install -r /app/runtime-requirements.txt

COPY . /app

CMD ["python", "/app/src/scheduler.py"]
