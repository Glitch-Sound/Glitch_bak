FROM python:slim-bookworm

ARG MODE=development
ENV MODE=$MODE

WORKDIR /app

COPY ./requirements.txt /app/requirements.txt

RUN apt update
RUN pip install --no-cache-dir --upgrade -r /app/requirements.txt

COPY ./entrypoint.sh /entrypoint.sh
RUN chmod +x /entrypoint.sh

ENTRYPOINT ["/entrypoint.sh"]
