FROM python:3.12-alpine

ENV PIP_NO_CACHE_DIR=off \
    WORK_DIR=/app

# Set the working directory
WORKDIR ${WORK_DIR}}

RUN apk add --no-cache build-base postgresql-dev

COPY requirements.txt ${WORK_DIR}/requirements.txt

RUN pip install --no-cache-dir -r ${WORK_DIR}/requirements.txt

COPY . ${WORK_DIR}

RUN echo ${WORK_DIR}
RUN chmod -R 700 ${WORK_DIR}

CMD ["sh", "-c", "${ENTRYFILE}"]
