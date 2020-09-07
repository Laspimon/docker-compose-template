FROM python:3.8-slim-buster

COPY ./requirements.txt /tmp/requirements.txt
RUN pip install -r /tmp/requirements.txt

VOLUME /data
ENV DATA_DIR /data

COPY . /app
ENV APP_DIR /app
WORKDIR ${APP_DIR}

CMD ["python", "app.py"]