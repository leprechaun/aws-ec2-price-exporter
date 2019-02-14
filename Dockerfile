FROM python:3-alpine as builder

RUN mkdir /app/
WORKDIR /app/

ADD ./ /app/

RUN pip install -r requirements.txt

RUN python prepare-data.py

RUN cat metrics

FROM nginx:alpine

COPY --from=builder /app/metrics /usr/share/nginx/html/
