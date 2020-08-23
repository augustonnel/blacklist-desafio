FROM python:3.8

WORKDIR /app

COPY app/requirements.txt .

RUN pip install -r requirements.txt

COPY app/src/ .

EXPOSE 5000
CMD ["python", "./server.py"]