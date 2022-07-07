FROM point8/ubuntu-focal-fossa-pyenv-poetry:v1
LABEL maintainer="Point 8 GmbH <kontakt@point-8.de>"

WORKDIR /app

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

EXPOSE 8501

ENTRYPOINT []
CMD ["poetry", "run", "streamlit", "run", "app.py"]
