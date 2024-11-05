#FROM python:3.11-slim AS build
#
#WORKDIR /workspace
#
#RUN apt-get update -qq && DEBIAN_FRONTEND=noninteractive apt-get -yq dist-upgrade && \
#  DEBIAN_FRONTEND=noninteractive apt-get install -yq --no-install-recommends \
#    gettext \
#    curl \
#    build-essential \
#    libpq-dev
#
#RUN curl -sSL https://pdm-project.org/install-pdm.py | python3 -
#
#COPY pdm.lock pyproject.toml .
#COPY pysvc pysvc
#RUN ~/.local/bin/pdm install --prod
#
#COPY . .
#
#FROM python:3.11-slim AS runtime
#
#RUN apt-get update -qq \
#    && DEBIAN_FRONTEND=noninteractive apt-get install -yq --no-install-recommends \
#        gettext \
#        curl \
#        libpq-dev
#
#COPY --from=build /workspace /workspace
#WORKDIR /workspace
#
#ARG VERSION
#ENV VERSION=$VERSION
#
#ENV EXCHANGE="portal"
#ENV PRODUCER="hr"
#
#ENV HOST="0.0.0.0"
#ENV PORT="5000"
#
#EXPOSE "${PORT}"
#
##CMD [ "./entrypoint.sh" ]



FROM python:3.11-slim AS build

WORKDIR /workspace

RUN apt-get update -qq && DEBIAN_FRONTEND=noninteractive apt-get -yq dist-upgrade && \
  DEBIAN_FRONTEND=noninteractive apt-get install -yq --no-install-recommends \
    gettext \
    curl \
    build-essential \
    libpq-dev

RUN pip install -U pdm

COPY pdm.lock pyproject.toml .
COPY pysvc pysvc
RUN pdm install --check --prod --no-editable

COPY . .

FROM python:3.11-slim AS runtime

RUN apt-get update -qq && DEBIAN_FRONTEND=noninteractive apt-get -yq dist-upgrade && \
  DEBIAN_FRONTEND=noninteractive apt-get install -yq --no-install-recommends \
    curl \
    libpq-dev

COPY --from=build /workspace /workspace

ENV PATH="/workspace/.venv/bin:$PATH"

WORKDIR /workspace

ARG VERSION
ENV VERSION $VERSION

ENV EXCHANGE "portal"
ENV PRODUCER "calendar"

ENV HOST "0.0.0.0"
ENV PORT "5000"

EXPOSE "${PORT}"

CMD [ "./entrypoint.sh" ]
