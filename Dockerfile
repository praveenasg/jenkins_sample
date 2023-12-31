FROM python:3.8

RUN apt-get update && apt-get install -y python3-pip
RUN pip3 install django
RUN pip3 install django-multiselectfield

COPY . /app

WORKDIR /app

EXPOSE 8000

CMD ["python3", "manage.py", "runserver", "0.0.0.0:8000"]