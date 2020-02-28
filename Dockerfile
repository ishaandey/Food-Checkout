FROM python:3.8.0-alpine
ENV PYTHONUNBUFFERED 1

# install psycopg2 dependencies
RUN apk update \
  && apk add postgresql-dev gcc python3-dev musl-dev

RUN mkdir /app
WORKDIR /app
COPY requirements.txt /app/
RUN pip install -r requirements.txt
COPY . /app/

# Wait for postgres container to be built before starting
ENTRYPOINT ["./entrypoint.sh"]