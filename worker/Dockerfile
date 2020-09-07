FROM python:3.8-slim-buster

COPY ./requirements.txt /tmp/requirements.txt
RUN pip install -r /tmp/requirements.txt

COPY . /app
ENV APP_DIR /app
WORKDIR ${APP_DIR}

CMD ["python", "worker.py"]