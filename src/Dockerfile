FROM python:3-buster

EXPOSE 80

COPY requirements.txt /app/requirements.txt
RUN pip install -r /app/requirements.txt


WORKDIR /mnt/python-code/

ENTRYPOINT [ "/mnt/python-code/starter.sh" ]