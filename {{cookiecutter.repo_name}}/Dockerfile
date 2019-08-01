FROM {{cookiecutter.docker_image}}
LABEL maintainer="{{cookiecutter.full_name}} <{{cookiecutter.email}}>"

ENV PYTHONUNBUFFERED=1
{% if "alpine" not in cookiecutter.docker_image -%}
ENV TINI_VERSION v0.18.0
ADD https://github.com/krallin/tini/releases/download/${TINI_VERSION}/tini /bin/tini
{%- endif %}

COPY pyproject.toml poetry.lock ./
RUN \
    {% if "alpine" in cookiecutter.docker_image -%}
    apk add --no-cache tini && \
    {%- else -%}
    chmod +x /bin/tini && \
    {%- endif %}
    wget -q -O - https://raw.githubusercontent.com/sdispater/poetry/master/get-poetry.py | python && \
    $HOME/.poetry/bin/poetry config settings.virtualenvs.create false && \
    $HOME/.poetry/bin/poetry --no-interaction install --no-dev && \
    rm -rf $HOME/.poetry pyproject.toml poetry.lock

WORKDIR /app
COPY {{cookiecutter.package_name}} ./{{cookiecutter.package_name}}

ENTRYPOINT [ "tini", "--", "python", "-m", "{{cookiecutter.package_name}}" ]
