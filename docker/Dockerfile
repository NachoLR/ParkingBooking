FROM python:3.7.4-alpine3.10
ENV PYTHONUNBUFFERED 1

RUN mkdir /app
ADD ./parkingmanager /app
ADD ./docker/entrypoint.sh /usr/local/bin/entrypoint
WORKDIR /app

RUN apk add --no-cache --virtual .build-deps gcc musl-dev postgresql-dev \
        jpeg-dev zlib-dev libjpeg-turbo-dev tesseract-ocr \
        && pip install -U pip \
        && pip install anybadge coverage \
		&& pip install -r requirements.txt

EXPOSE 8080

ENTRYPOINT ["entrypoint"]
CMD ["runserver"]
