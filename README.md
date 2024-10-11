# ProHiredUsers 🚀

**ProHiredUsers** is a user management service designed as part of the ProHired platform. This service is responsible for handling user-related operations, including registration, authentication, profile management, and user roles. It is built using **Python** and follows a **RESTful architecture** to ensure scalability and maintainability. This project leverages **Docker** for containerization, **Alembic** for migrations, and CI/CD pipelines for automated testing and deployment.

## Key Features 🔑✨

- **User Registration and Authentication**: Users can register, log in, and manage their profiles. The authentication mechanism is based on **JWT (JSON Web Tokens)**.
- **Role-Based Access Control**: This service handles different user roles and permissions (e.g., admin, user, recruiter) to ensure access control across the platform.
- **Profile Management**: Users can update their personal information, such as name, email, and profile picture.
- **Password Management**: Secure password hashing with **bcrypt** and password reset functionality.
- **Database Migrations**: Uses **Alembic** for handling database schema changes.
- **Docker**: The service runs in a **Docker** container for easy setup and deployment.
- **CI/CD**: Automated testing and deployment using **GitLab CI/CD**.

## Technologies Used 🛠️

- **Python**: The core programming language for the service.
- **Flask**: A lightweight web framework that powers the REST API.
- **SQLAlchemy**: ORM for database interactions.
- **Alembic**: Database migration tool.
- **PostgreSQL**: The relational database used for storing user data.
- **Docker**: Used for containerization of the application.
- **GitLab CI/CD**: Continuous integration and deployment pipeline for automated testing and deployment.

## Folder Structure 📂

```plaintext
ProHiredUsers/
│
├── docker/                   # Docker-related files
├── migrations/               # Alembic migrations
├── src/                      # Source code for the application
│   ├── auth/                 # Authentication-related logic (JWT, bcrypt)
│   ├── models/               # SQLAlchemy models for user management
│   ├── routes/               # Flask routes for user-related API endpoints
│   ├── services/             # Business logic for user management
│   ├── utils/                # Helper functions (e.g., token generation, hashing)
│   └── __init__.py           # Flask app initialization
├── tests/                    # Unit tests for the application
│   ├── test_auth.py          # Tests for authentication functionality
│   ├── test_profile.py       # Tests for user profile management
│   └── test_roles.py         # Tests for role-based access control
├── .gitignore                # Git ignore file
├── .gitlab-ci.yml            # CI/CD pipeline for automated testing and deployment
├── Dockerfile                # Dockerfile for building the image
├── docker-compose.yml        # Docker Compose file for setting up the environment
├── alembic.ini               # Alembic configuration file
├── config.py                 # Application configuration file
├── requirements.txt          # Python dependencies
├── pytest.ini                # Pytest configuration file
└── README.md                 # Project README file
