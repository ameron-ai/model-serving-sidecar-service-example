FROM python:3.8-slim-buster

COPY requirements.txt /temp/requirements.txt
RUN pip3 install -r /temp/requirements.txt

RUN mkdir /service
COPY service/* /service/
WORKDIR /service

CMD ["uvicorn", "main:app", "--host", "0.0.0.0"]
