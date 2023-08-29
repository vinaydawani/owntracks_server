FROM python:3.11.3-slim-bullseye
# -slim-bullseye

RUN addgroup --system --gid 1000 owntracks && adduser --system -u 1000 --group owntracks

WORKDIR /owntracks_server/
RUN chown owntracks:owntracks /owntracks_server/

ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1
ENV ENVIRONMENT prod
# ENV TESTING 0

COPY ./requirements.txt /owntracks_server/
RUN pip install --no-cache-dir -r requirements.txt

COPY --chown=owntracks:owntracks . .
RUN chmod +x run.sh

ENV PYTHONPATH=/owntracks_server
EXPOSE 8000

USER owntracks

HEALTHCHECK --interval=30s --retries=3 \
  CMD curl --fail http://localhost/api/v1/hc/db || exit 1

CMD ["./run.sh"]