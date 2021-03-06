FROM python:3.7
ADD ./backend /code
COPY ./requirements.txt /code/
WORKDIR /code
RUN pip install -r requirements.txt
CMD python manage.py migrate \
    && python manage.py runserver 0.0.0.0:5000
EXPOSE 5000