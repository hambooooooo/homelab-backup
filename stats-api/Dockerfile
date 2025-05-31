FROM python:3.12-slim

WORKDIR /app
COPY . .

RUN pip install flask flask-cors psutil

EXPOSE 1337

CMD ["python3", "stats-api.py"]
