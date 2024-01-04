FROM python:3.12-bullseye

WORKDIR /app

COPY ./requirements.txt requirements.txt

RUN pip install --no-cache-dir --upgrade -r requirements.txt

COPY ./app /app/app

CMD ["uvicorn", "app.main:app", "--proxy-headers", "--host", "0.0.0.0", "--port", "80"]

EXPOSE 80

## Commands:
# docker build -t simpleapp .
# docker run -d --name test-run-01 -p 80:80 simpleapp
# check docker logs and run exec commnds

