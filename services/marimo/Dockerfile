FROM point8/ubuntu-jammy-jellyfish-pyenv-poetry:v2
LABEL maintainer="Point 8 GmbH <kontakt@point-8.de>"

WORKDIR /app

COPY .python-version .
RUN pyenv install -s "$(cat .python-version)" &&\
    pyenv global "$(cat .python-version)" &&\
    pyenv local "$(cat .python-version)" &&\
    pyenv versions

RUN ls -lah && pyenv versions

COPY pyproject.toml poetry.lock ./

RUN poetry install &&\
    poetry run python --version

COPY . ./

EXPOSE 8080

RUN useradd -m point8
USER point8

ENTRYPOINT []
CMD ["poetry", "run", "marimo", "run", "notebook.py", "--host", "0.0.0.0", "--port", "8080", "--headless"]
