FROM python:3.9

ENV PIP_DEFAULT_TIMEOUT=100 \
    PIP_DISABLE_PIP_VERSION_CHECK=1 \
    PIP_NO_CACHE_DIR=1 \
    POETRY_NO_INTERACTION=1 \
    POETRY_VIRTUALENVS_CREATE=false \
    POETRY_VERSION=1.1.11

RUN pip install "poetry==$POETRY_VERSION"

WORKDIR /ktest
RUN mkdir -p /ktest/reports

ADD *.toml *.lock ./
ADD ./features ./features

RUN poetry install

CMD ["behave", "--junit"]
