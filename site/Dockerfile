FROM python:3.9 AS build

RUN python3 -m venv /opt/venv
ENV PATH="/opt/venv/bin:$PATH"

RUN pip install --upgrade pip
RUN pip install gunicorn==20.1.0
COPY requirements.txt /home
RUN pip install -r home/requirements.txt --no-cache-dir

FROM python:3.9.6-slim-buster

COPY --from=build /opt/venv /opt/venv
ENV PATH="/opt/venv/bin:$PATH"

WORKDIR /home/project
