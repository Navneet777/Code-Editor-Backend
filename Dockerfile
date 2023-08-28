# Dockerfile

FROM python:3.9

ENV PYTHONUNBUFFERED 1

RUN mkdir /code
WORKDIR /code

COPY requirements.txt /code/
RUN pip install --upgrade pip
RUN pip install -r requirements.txt
RUN pip install twisted[http2,tls]
COPY . /code/
ENV DJANGO_SETTINGS_MODULE=code_editor_backend.settings

EXPOSE 8000
CMD ["daphne", "code_editor_backend.asgi:application", "-b", "0.0.0.0", "-p", "8000"]
