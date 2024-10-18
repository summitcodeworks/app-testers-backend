# App Testers Backend

The **App Testers Backend** is a Flask-based API application designed for managing apps, users, and their interactions. It provides CRUD operations for app-related data and user details, along with API key authentication.

## Features

- Create, update, delete, and search apps.
- Manage users, including user registration and updates.
- API key validation for secure endpoints.
- Search functionality for apps based on various filters (app name, developer name, package name).

## Prerequisites

- Python 3.8+
- Flask
- SQLAlchemy (for database ORM)
- PostgreSQL (or any other supported database)

## Installation

1. Clone the repository:

    ```bash
    git clone https://github.com/debarunlahiri/app-testers-backend.git
    ```

2. Navigate to the project directory:

    ```bash
    cd app-testers-backend
    ```

3. Set up a virtual environment:

    ```bash
    python3 -m venv venv
    source venv/bin/activate  # On Windows: venv\Scripts\activate
    ```

4. Install the required dependencies:

    ```bash
    pip install -r requirements.txt
    ```

5. Set up the environment variables:

    ```bash
    export FLASK_APP=app
    export FLASK_ENV=development
    ```

6. Configure the database in `config.py` with your database URI.

7. Initialize the database:

    ```bash
    flask db upgrade
    ```

## API Endpoints

### Apps

- **GET** `/app-lists`: Retrieve a list of all apps.
- **POST** `/create-app`: Create a new app.
- **GET** `/app-detail/<int:id>`: Get app details by ID.
- **PUT** `/apps/<int:id>`: Update an app by ID.
- **DELETE** `/apps/<int:id>`: Delete an app by ID.
- **GET** `/search-apps`: Search apps by app name, developer name, or package name.

### Users

- **POST** `/register-user`: Register a new user.
- **GET** `/users`: Get all registered users.
- **GET** `/users/<int:id>`: Get user details by ID.
- **PUT** `/users/<int:id>`: Update a user by ID.
- **DELETE** `/users/<int:id>`: Delete a user by ID.

### API Key Authentication

All routes require a valid `user_key` in the request headers for authentication:

```bash
Authorization: user_key <your_api_key>
