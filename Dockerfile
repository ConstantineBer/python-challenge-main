FROM python:3.8-slim

WORKDIR /code

ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

RUN pip install pipenv
COPY ./Pipfile /code/Pipfile
COPY ./Pipfile.lock /code/Pipfile.lock
RUN pipenv install --system --deploy --ignore-pipfile

COPY ./app /code/app
COPY ./controllers /code/controllers
COPY ./pages /code/pages
ENV PYTHONPATH=/code

CMD ["python", "app/main.py"]