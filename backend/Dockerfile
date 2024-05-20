FROM python:3.11

ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

RUN mkdir /backend
WORKDIR /backend

COPY requirements.txt /backend/

RUN pip install pipenv && pip install -r requirements.txt

COPY . /backend/

RUN python manage.py migrate && python manage.py collectstatic --no-input && python manage.py createsuperuser

CMD ["python", "manage.py", "runserver", "0.0.0.0:8000"]
