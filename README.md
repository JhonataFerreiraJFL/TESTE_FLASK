# Flask Study Project

## Overview

This repository contains a Flask project developed as part of my journey to master the Flask web framework. The project focuses on building a web application from the ground up, exploring various features of Flask, such as routing, templating, database integration, and deployment.

## Features

- User registration and authentication system.
- CRUD operations for managing resources.
- Integration with a SQL database using SQLAlchemy.
- Templating with Jinja2 for dynamic HTML pages.
- RESTful API endpoints.
- Static file management (CSS, JavaScript, images).
- Deployment configurations for both development and production environments.

## Structure

- **app/**: The main Flask application directory.
  - **models.py**: SQLAlchemy models for the database.
  - **routes.py**: Application routes and views.
  - **forms.py**: WTForms for handling user input.
  - **templates/**: Jinja2 templates for rendering HTML.
  - **static/**: Static files like CSS, JavaScript, and images.
  - **auth/**: Authentication and user management.
  - **config.py**: Configuration settings for the application.
- **migrations/**: Database migration files.
- **tests/**: Unit tests for the application.
- **instance/**: Instance-specific configurations.
- **requirements.txt**: Python dependencies.

## Getting Started

### Prerequisites

- Python 3.8 or higher
- Flask
- SQLAlchemy
- WTForms
- PostgreSQL (or any preferred SQL database)

### Installation

1. Clone the repository:

   ```bash
   git clone https://github.com/JhonataFerreiraJFL/TESTE_FLASK.git
   cd TESTE_FLASK
