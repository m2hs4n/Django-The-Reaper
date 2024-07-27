# Django Project

## Table of Contents
- [Introduction](#introduction)
- [Features](#features)
- [Project Structure](#project-structure)
- [Setup](#setup)
  - [Development Setup](#development-setup)
  - [Production Setup](#production-setup)
  - [Running Tests](#running-tests)
- [Usage](#usage)
- [Contributing](#contributing)
- [License](#license)

## Introduction
This project features a customized Django setup designed to streamline the development and deployment process. The structure and configuration are tailored to facilitate easy adaptation to your own projects. The project is Dockerized for both development and production environments, with dedicated Docker Compose configurations to simplify setup and deployment.

## Features
- Dockerized for development and production environments
- Separate settings for development and production
- Easy environment management with dedicated `.env` files for each environment
- Optimized for security and performance in production
- Comprehensive setup instructions
- Example app to demonstrate basic functionality with organized models

## Technologies Used
![Python](https://img.shields.io/badge/python-3670A0?style=for-the-badge&logo=python&logoColor=ffdd54)
![Django](https://img.shields.io/badge/django-092E20?style=for-the-badge&logo=django&logoColor=white)
![Django REST Framework](https://img.shields.io/badge/Django_REST-ff1709?style=for-the-badge&logo=django&logoColor=white&color=ff1709&labelColor=gray)
![Docker](https://img.shields.io/badge/docker-2496ED?style=for-the-badge&logo=docker&logoColor=white)
![GitLab CI](https://img.shields.io/badge/GitLabCI-330F63?style=for-the-badge&logo=gitlab&logoColor=white)

## Project Structure
```plaintext
├── project_name
│   ├── __init__.py
│   ├── settings
│   │   ├── __init__.py
│   │   ├── base.py
│   │   ├── development.py
│   │   └── production.py
│   ├── urls.py
│   └── wsgi.py
├── apps
│   ├── example
│   │   ├── __init__.py
│   │   ├── admin.py
│   │   ├── apps.py
│   │   ├── models
│   │   │   ├── __init__.py
│   │   │   ├── profile.py
│   │   │   └── user.py
│   │   ├── tests.py
│   │   └── views.py
│   └── ...
├── manage.py
├── requirements
│   ├── base.txt
│   ├── development.txt
│   └── production.txt
├── static
│   └── ...
├── templates
│   └── ...
├── envs
│   ├── development
│   │   └── .env
│   └── production
│       └── .env
├── Dockerfile
├── docker-compose
│   ├── development.yml
│   ├── production.yml
│   └── test.yml
└── README.md
```
## Description

### Django Customize for Development and Production
The Django project is customized to cater to both development and production environments. This includes different settings, Docker configurations, and `.env` files for each environment.

### Models Directory Structure
To maintain a clean and organized codebase, each app's models are separated into individual files within a dedicated `models` directory. This modular approach ensures better manageability and scalability of the code.


### Settings Customize
The Django settings are split into multiple files to manage configurations for different environments effectively. This modular approach ensures that settings specific to development and production environments are isolated, providing better manageability.

- **base.py**: Contains settings common to all environments, such as installed apps, middlewares and templates.
- **development.py**: Includes settings specific to the development environment. This file typically has configurations suitable for debugging, such as `DEBUG = True`, secrect-key, `ALLOWED_HOSTS = ["*"]`, database configurations, development-specific installed apps, and other settings that facilitate local development.
- **production.py**: Contains settings for the production environment This includes settings like `DEBUG = False`, allowed hosts, and database configurations.

- **Development Environment**:
  - Optimized for debugging and local testing.
  - Includes development tools and middleware.
  - Uses a development-specific `envs/develop/.env` file to manage environment variables.
  - Docker Compose configuration (`docker-compose.develop.yml`) for development sets up services with settings suitable for a development workflow.

- **Production Environment**:
  - Focuses on performance and stability.
  - Includes optimized database settings, and caching mechanisms.
  - Uses a production-specific `envs/production/.env` file to manage environment variables securely.
  - Docker Compose configuration (`docker-compose.production.yml`) for production ensures that services are set up with production-ready settings.

### Venv Files
Virtual environments (`venv`) are used to create isolated Python environments for the project. This ensures that dependencies required for the project do not interfere with system-wide Python packages or other projects.

- **Creating a Virtual Environment**:
  - A virtual environment is created using `python -m venv venv` to ensure that project-specific dependencies are isolated.
  - The virtual environment is activated using `source venv/bin/activate` on Unix or `venv\Scripts\activate` on Windows.

### Requirements Files
The project uses multiple requirements files to manage dependencies for different environments efficiently. This approach ensures that only the necessary dependencies are installed for each environment, keeping the project lean.

- **base.txt**: Lists the core dependencies required for the project across all environments.
- **development.txt**: Includes additional dependencies needed for development, such as testing frameworks and debugging tools. It also includes the `production.txt` file to ensure all base dependencies are installed.
- **production.txt**: Lists dependencies required for the production environment, focusing on performance and security. It also includes the `base.txt` file to ensure all base dependencies are installed.
