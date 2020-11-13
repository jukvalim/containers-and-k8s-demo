FROM python:3.8-slim

COPY ./src/requirements.txt .
RUN pip install -r requirements.txt

COPY ./src /app
WORKDIR /app

EXPOSE 8000
ENTRYPOINT ["gunicorn", "app:app", "-b", "0.0.0.0:8000"]

