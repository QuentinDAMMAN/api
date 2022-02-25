ARG VERSION_PYTHON

FROM python:latest

WORKDIR /App

COPY . .

RUN pip install -r requirements.txt

EXPOSE 5000

CMD ["flask","run","--host=0.0.0.0"]
