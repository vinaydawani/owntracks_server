FROM python:3.11.3-slim-bullseye
# -slim-bullseye

RUN addgroup --system owntracks && adduser --system --group owntracks

WORKDIR /owntracks_server/

ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1
ENV ENVIRONMENT prod
# ENV TESTING 0

COPY ./requirements.txt /owntracks_server/
RUN pip install -r requirements.txt

COPY . .

RUN chmod +x run.sh

ENV PYTHONPATH=/owntracks_server

RUN chown -R owntracks:owntracks /owntracks_server/

USER owntracks

EXPOSE 8000

CMD ["./run.sh"]