FROM python:3.7.0

RUN groupadd --gid 1001 app && useradd -u 1001 -g app app

RUN mkdir /app && chown app /app
WORKDIR /app

COPY --chown=app ./Pipfile /app/Pipfile
COPY --chown=app ./Pipfile.lock /app/Pipfile.lock
RUN pip install pipenv~=11.10.0 && \
    pipenv install --system --deploy

COPY --chown=app ./ /app/

USER 1001

ENTRYPOINT ["./docker/entrypoint.sh"]
