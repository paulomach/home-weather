FROM python:3.9-alpine

ENV PYTHONUNBUFFERED 1

COPY . /app

RUN pip install -r /app/runtime-requirements.txt

CMD ["python", "/app/src/scheduler.py"]
