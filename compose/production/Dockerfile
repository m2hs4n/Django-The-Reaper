# # Official Python image
# FROM python:3.10-slim

# # Environment variables
# ENV PYTHONDONTWRITEBYTECODE=1
# ENV PYTHONUNBUFFERED=1

# # Work directory
# WORKDIR /app

# # Installing dependencies
# COPY requirements /app/
# RUN pip install --upgrade pip
# RUN pip install -r develop.txt

# # Copy project files
# COPY . /app/

# # Copy and set permission to entrypoint.sh
# COPY ./compose/develop/maintenances/entrypoint.sh /entrypoint.sh
# RUN chmod +x /entrypoint.sh

# # Run the entrypoint script
# # ENTRYPOINT ["/entrypoint.sh"]

# # Expose port 8000
# # EXPOSE 8000

# # Run porject
# # This command reload with every edit file in project
# # CMD ["sh", "-c", "python manage.py runserver --develop 0.0.0.0:8000"]


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

# Copy and set permission to entrypoint.sh
COPY ./compose/production/maintenances/entrypoint.sh /entrypoint.sh
RUN chmod +x /entrypoint.sh

# Run the entrypoint script
ENTRYPOINT ["/entrypoint.sh"]

# Expose the port on which Django runs
EXPOSE 8000

# Run Django with Gunicorn (adjust according to your setup)
CMD ["gunicorn", "--workers=3", "--bind", "0.0.0.0:8000", "config.wsgi:application"]
