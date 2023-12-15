FROM python:3.11.5

ENV PYTHONUNBUFFERED 1

WORKDIR /app

COPY requirements.txt .

RUN pip install -r requirements.txt

COPY . .

EXPOSE 8000

# run this django.sh file
ENTRYPOINT ["/app/django.sh"]