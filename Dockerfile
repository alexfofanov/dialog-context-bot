FROM python:3.12-slim

RUN apt-get update && \
    apt-get install -y libpq-dev gcc && \
    rm -rf /var/lib/apt/lists/*

COPY --from=ghcr.io/astral-sh/uv:latest /uv /uvx /bin/

WORKDIR /app

COPY . /app

RUN uv sync --frozen --no-cache
ENV PATH="/app/.venv/bin:$PATH"

CMD ["python", "-m", "src.main"]
