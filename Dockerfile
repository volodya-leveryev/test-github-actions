FROM python:3.10-slim
WORKDIR /web
COPY . .
EXPOSE 8000
RUN pip install django
RUN python manage.py migrate
CMD python manage.py runserver 0.0.0.0:8000
