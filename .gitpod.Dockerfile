FROM gitpod/workspace-full

USER gitpod

RUN curl -sSL https://raw.githubusercontent.com/python-poetry/poetry/master/get-poetry.py | python -

ENV PATH=/home/gitpod/.poetry/bin:$PATH