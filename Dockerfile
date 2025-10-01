FROM python:3.13.7-slim-bookworm

RUN pip install pipenv

WORKDIR /app

COPY Pipfile Pipfile.lock ./

RUN pipenv install --deploy --system

COPY . .

CMD ["python", "src/main.py"]
