# Render Deployment Dockerfile
FROM python:3.11.9-slim

# Set environment variables
ENV PYTHONDONTWRITEBYTECODE=1
ENV PYTHONUNBUFFERED=1
ENV DEBIAN_FRONTEND=noninteractive

# Set work directory
WORKDIR /app

# Install system dependencies
RUN apt-get update \
    && apt-get install -y --no-install-recommends \
        build-essential \
        curl \
        && apt-get clean \
        && rm -rf /var/lib/apt/lists/*

# Install Python dependencies
COPY requirements.txt constraints.txt ./
RUN pip install --no-cache-dir --upgrade pip==24.0 setuptools==69.5.1 wheel==0.42.0 \
    && pip install --no-cache-dir -c constraints.txt -r requirements.txt

# Copy project files
COPY . .

# Create necessary directories
RUN mkdir -p /app/staticfiles /app/media

# Collect static files
RUN python manage.py collectstatic --noinput

# Create non-root user for security
RUN adduser --disabled-password --gecos '' renderuser \
    && chown -R renderuser:renderuser /app
USER renderuser

# Expose port (Render assigns PORT automatically)
EXPOSE $PORT

# Start command
CMD gunicorn --bind 0.0.0.0:$PORT --workers 2 --timeout 120 portfolio_site.wsgi:application 

