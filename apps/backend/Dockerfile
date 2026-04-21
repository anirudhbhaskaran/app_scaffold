FROM python:3.12-slim

# Python 3.14 is not yet available as a stable slim image; 3.12 is the current
# production-ready slim. Update the tag when 3.14-slim is published.

WORKDIR /app

# System deps for compiled extensions (motor, cryptography, etc.)
RUN apt-get update && apt-get install -y --no-install-recommends \
    curl \
    build-essential \
    libssl-dev \
    && rm -rf /var/lib/apt/lists/*

# Install Python deps before copying source so layer is cached
COPY pyproject.toml ./
RUN pip install --no-cache-dir -e ".[dev]"

# COPY . .

EXPOSE 8000

CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "8000"]
