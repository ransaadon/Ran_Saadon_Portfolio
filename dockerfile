FROM python:3.13.0a6-alpine3.18

WORKDIR /app

COPY ./requirements.txt /app/
COPY ./app.py /app/
RUN pip install  --no-cache-dir -r requirements.txt

CMD ["flask", "run", "--host", "0.0.0.0"]


