FROM --platform=$BUILDPLATFORM arm64v8/python:3.12.0rc2-alpine3.18 AS builder
WORKDIR /timskiproekt

# Set environment variables
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

# Install psycopg2 dependencies
RUN apk update && apk add postgresql-dev gcc python3-dev musl-dev

# Install dependencies
COPY requirements.txt /timskiproekt
RUN pip3 install -r requirements.txt --no-cache-dir

# copy entrypoint.sh
COPY entrypoint.sh .
RUN sed -i 's/\r$//g' /timskiproekt/entrypoint.sh
RUN chmod +x /timskiproekt/entrypoint.sh

COPY timskiproekt /timskiproekt

# run entrypoint.sh
ENTRYPOINT ["/timskiproekt/entrypoint.sh"]