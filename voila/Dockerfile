FROM ubuntu:20.04
LABEL maintainer="Point 8 GmbH <kontakt@point-8.de>"

WORKDIR /app

# No user feedback during installation
ENV DEBIAN_FRONTEND=noninteractive
ENV TZ=Europe/Berlin

ENV LANG en_US.UTF-8
ENV LANGUAGE en_US:en
ENV LC_ALL en_US.UTF-8

# PYTHON, PYENV, POETRY
ARG PYENV_INSTALLER="https://raw.githubusercontent.com/pyenv/pyenv-installer/master/bin/pyenv-installer"
ARG POETRY_INSTALLER="https://install.python-poetry.org"

ENV CI=true
ENV PYENV_ROOT="/.pyenv"
ENV POETRY_HOME="/.poetry"
ENV PATH="${POETRY_HOME}/bin:${PYENV_ROOT}/shims:${PYENV_ROOT}/bin:${PATH}"
ENV PYTHONDONTWRITEBYTECODE=1

SHELL ["/bin/bash", "-o", "pipefail", "-c"]
RUN apt-get update -y &&\
    apt-get upgrade -y &&\
    apt-get --no-install-recommends -y install \
      build-essential \
      bzip2 \
      ca-certificates\
      checkinstall \
      cmake \
      curl \
      gettext \
      git \
      libbz2-dev \
      libc6-dev \
      libffi-dev \
      libgdbm-dev \
      libncursesw5-dev \
      libpangocairo-1.0-0 \
      libreadline-gplv2-dev \
      libsqlite3-dev \
      libssl-dev \
      locales \
      make \
      openssh-client \
      openssl \
      python3-distutils \
      python3-pip \
      python3-venv \
      rsync \
      software-properties-common \
      tk-dev \
      tzdata \
      wget \
      zlib1g-dev &&\
    rm -rf /var/lib/apt/lists/* &&\
    ln -sfn /usr/bin/python3.8 /usr/bin/python &&\
    ln -sfn /usr/bin/pip3 /usr/bin/pip &&\
    python --version &&\
    pip --version &&\
    ln -fs /usr/share/zoneinfo/$TZ /etc/localtime &&\
    dpkg-reconfigure -f noninteractive tzdata &&\
    locale-gen ${LANG} &&\
    curl -L $PYENV_INSTALLER | bash &&\
    curl -sSL $POETRY_INSTALLER | python &&\
    poetry config virtualenvs.in-project true

COPY .python-version .
RUN pyenv install -s "$(cat .python-version)" &&\
    pyenv global "$(cat .python-version)" &&\
    pyenv local "$(cat .python-version)" &&\
    pyenv versions

RUN ls -lah && pyenv versions

COPY pyproject.toml poetry.lock ./

RUN poetry env use "$(cat .python-version)" &&\
    poetry install &&\
    poetry run python --version

COPY . ./

EXPOSE 8866

ENTRYPOINT []
CMD ["poetry", "run", "voila", "example.ipynb"]
