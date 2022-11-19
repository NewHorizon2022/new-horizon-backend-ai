FROM python:3-buster

EXPOSE 80
WORKDIR /app/live

COPY requirements.txt /app/live/requirements.txt
RUN pip install -r /app/live/requirements.txt

COPY . /app/live

RUN ["chmod", "+x", "/app/live/starter.sh"]
ENTRYPOINT [ "/app/live/starter.sh" ]