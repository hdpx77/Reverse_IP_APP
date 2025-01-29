
FROM python:3.12.3


WORKDIR /app


COPY app.py requirements.txt ./


RUN pip install -r requirements.txt


EXPOSE 8080


CMD ["python", "app.py"]
