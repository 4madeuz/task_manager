FROM python:3.10

WORKDIR /opt/app

ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1
ENV UWSGI_PROCESSES 1
ENV UWSGI_THREADS 16
ENV UWSGI_HARAKIRI 240
ENV DJANGO_SETTINGS_MODULE 'app.settings'


RUN apt-get update && apt-get install -y postgresql-client

COPY run_uwsgi.sh run_uwsgi.sh
COPY requirements.txt requirements.txt
COPY uwsgi/uwsgi.ini uwsgi.ini

RUN mkdir -p /opt/app/static/ \
    && mkdir -p /opt/app/media/ \
    && pip install --upgrade pip \
    && pip install -r requirements.txt

COPY . .

EXPOSE 8000

ENTRYPOINT ["sh", "run_uwsgi.sh"]
