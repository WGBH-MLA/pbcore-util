FROM python:3.12-bookworm
COPY --from=ghcr.io/astral-sh/uv:latest /uv /uvx /bin/

# Change the working directory to the `app` directory
WORKDIR /app

# Copy the project into the image
ADD . /app

# Sync the project
RUN uv sync

CMD ["uv", "run", "gunicorn", "-c", "gunicorn_conf.py", "app.main:app"]
