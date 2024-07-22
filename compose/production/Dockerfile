# Use an official Python runtime as a parent image
FROM python:3.10-slim

# Set environment variables
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

# Set working directory in the container
WORKDIR /app

# Install system dependencies
RUN apt-get update \
    && apt-get install -y --no-install-recommends \
        libpq-dev \
    && rm -rf /var/lib/apt/lists/*

# Install Python dependencies
COPY requirements /app/
RUN pip install --no-cache-dir -r production.txt

# Copy project files into the container
COPY . /app/

# Copy and set permission for running celery flower
COPY ./compose/production/test/test.sh /start-test.sh
RUN chmod +x /start-test.sh

# Copy and set permission to entrypoint.sh
COPY ./compose/production/maintenances/entrypoint.sh /entrypoint.sh
RUN chmod +x /entrypoint.sh

# Run the entrypoint script
ENTRYPOINT ["/entrypoint.sh"]

# Expose the port on which Django runs
EXPOSE 8000

# Run Django with Gunicorn (adjust according to your setup)
CMD ["gunicorn", "--workers=3", "--bind", "0.0.0.0:8000", "config.wsgi:application"]
