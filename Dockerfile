FROM python:3.10-slim
WORKDIR /web
COPY . .
EXPOSE 8000
RUN pip install django
CMD python manage.py runserver
