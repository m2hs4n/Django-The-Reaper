# Django The Reaper

## Table of Contents
- [Introduction](#introduction)
- [Key Features](#key-features)
- [Features](#features)
- [Technologies Used](#technologies-used)
- [Project Structure](#project-structure)
- [Description](#description)
- [Usage](#usage)

## Introduction
Welcome to the Django Project! This repository contains a customized Django setup designed to streamline both development and production workflows. The project has been structured to offer a clean and scalable codebase, making it easy to adapt and extend for your own needs.

### Key Features:
- **Modular Settings**: The Django settings are divided into separate files for base, development, and production configurations. This separation ensures that you can manage environment-specific settings efficiently.
- **Organized Models**: Each app within the project follows a modular approach where models are organized into a dedicated `models` directory. Each model is defined in its own file, promoting cleaner code and better maintainability.
- **Dockerized Setup**: The project is Dockerized for both development and production environments, with dedicated Docker Compose configurations. This setup simplifies the process of building, deploying, and managing the application across different environments.
- **Environment Management**: Separate `.env` files are used for development and production, making it easy to manage environment-specific variables and keep sensitive information secure.
- **Requirements Management**: Dependencies are managed through multiple requirements files, ensuring that the correct packages are installed for each environment (base, development, production).

This project is designed to be easily adaptable and extendable, providing a solid foundation for developing robust Django applications. Whether you are working on a local development setup or deploying to production, this structure ensures that you have a scalable and maintainable codebase.

⭐ Feel free to explore the project, and don't hesitate to reach out if you have any questions or need assistance. ❤️


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
│   └── production.txtz
├── envs
│   ├── develop
│   │   └── .env
│   └── production
│       └── .env
├── Dockerfile
├── docker-compose
│   ├── development.yml
│   ├── production.yml
│   └── test.yml
├── docker-compose.develop.yml
├── docker-compose.production.yml
├── docker-compose.tests.yml
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

<!-- ### Usage
- **Development**: Run project for development that can see all of  -->

## Usage

This project includes three Docker Compose configurations to manage different environments effectively: development, production, and testing. Below are the instructions on how to use each of these configurations.

### Development

For development, use the `docker-compose.develop.yml` configuration. This setup is optimized for local development and debugging. Logs are visible in the terminal to aid in real-time debugging.

1. **Create a superuser (optional)**:
    ```sh
    docker-compose -f docker-compose.develop.yml run web python manage.py createsuperuser
    ```

2. **Build and run the Docker containers for development**:
    ```sh
    docker-compose -f docker-compose.develop.yml up --build
    ```

3. **Access the application**:
    - Open your browser and navigate to `http://localhost:8000` to see the development server in action.

**Note**: Do not use the `-d` (detached) flag with the development configuration to ensure that you can view logs and debug output directly in the terminal.

### Production

For production, use the `docker-compose.production.yml` configuration. This setup is optimized for performance and security and is intended for deployment in a production environment.

1. **Chagne .env variables**:

    **<u>Change the variables inside the .env file for security</u>**

2. **Create a superuser (optional)**:
    ```sh
    docker-compose -f docker-compose.production.yml run web python manage.py createsuperuser
    ```

3. **Build and run the Docker containers for production**:
    ```sh
    docker-compose -f docker-compose.production.yml up --build -d
    ```

4. **Access the application**:
    - The application will be accessible at `http://localhost:8000` or your configured production domain.

**Note**: Ensure that your production environment variables and configurations are change in the `.env` file located in the `envs/production` directory.

### Running Tests

For running tests, use the `docker-compose.test.yml` configuration. This setup is designed to run your test suite in an isolated environment.

1. **Build and run the Docker containers for testing**:
    ```sh
    docker-compose -f docker-compose.test.yml up --build
    ```

**Note**: The `docker-compose.test.yml` configuration is optimized for running tests and does not require manual intervention for test execution.

By using these Docker Compose configurations, you can manage different
