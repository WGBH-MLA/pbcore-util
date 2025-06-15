FROM python:3.11-slim

# Install system dependencies
RUN apt-get update && apt-get install -y \
    libxml2-dev libxslt1-dev gcc \
    && rm -rf /var/lib/apt/lists/*

# Set working directory
WORKDIR /app

# Install Python dependencies
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Copy the FastAPI app
COPY . .

# Run with Gunicorn and Uvicorn workers
CMD ["gunicorn", "-c", "gunicorn_conf.py", "app.main:app"]
