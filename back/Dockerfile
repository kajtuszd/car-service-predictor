FROM python:3.8

ENV PYTHONUNBUFFERED 1

RUN mkdir /back
WORKDIR /back

COPY  . /back/

RUN apt-get update

RUN pip install --upgrade pip
RUN pip install -r requirements.txt

ENTRYPOINT ["python3", "manage.py"]
CMD ["runserver", "0.0.0.0:8080"]
