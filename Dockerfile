# syntax=docker/dockerfile:1
# Suite image: installs mcp-test-harness from PyPI + this repo's connectors.
# Build:  docker build -t mcp-test-suite:local .
# Dev:    docker build -t mcp-test-suite:dev --target dev .

FROM python:3.12-slim-bookworm AS base

ENV PYTHONDONTWRITEBYTECODE=1 \
    PYTHONUNBUFFERED=1

WORKDIR /app

COPY pyproject.toml README.md LICENSE NOTICE CITATION.cff ./
COPY src ./src

# Engine from PyPI; connectors (declarative + CLI wrapper) from this build.
RUN pip install --no-cache-dir --upgrade pip && \
    pip install --no-cache-dir "mcp-test-harness>=3.0.9,<4" && \
    pip install --no-cache-dir .

FROM base AS dev
RUN pip install --no-cache-dir ".[dev]"
ENTRYPOINT ["mcp-suite"]
CMD ["--help"]

FROM base AS runtime
ENTRYPOINT ["mcp-suite"]
CMD ["--help"]
