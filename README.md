
# User Admin RESTful API

This project aims to develop a RESTful API following Test-Driven Development (TDD) principles. Utilizing Python and Flask, the API adheres to RESTful design standards, employing basic HTTP methods such as GET, POST, PUT, and DELETE. Endpoints are structured to perform CRUD operations on user data, allowing retrieval of all users, individual user details, addition, updating, and deletion of users. Leveraging Docker streamlines local development setup and deployment processes, ensuring consistency across environments. SQLAlchemy facilitates interactions with a PostgreSQL database, enhancing data management capabilities. Test suites are crafted with pytest, emphasizing unit and integration testing for robust API validation. Version control and collaboration are managed through GitLab, integrating Continuous Integration (CI) pipelines to automate testing and ensure code quality before deployment to Heroku. Each component contributes to the project's overarching goal of building a scalable, reliable, and maintainable RESTful API.


## Acknowledgements

 - [testdriven.io](https://testdriven.io)



## Deployment

To deploy this project run:
```bash
  docker-compose up -d
```
To run the tests:
```bash
docker-compose exec api python -m pytest "src/tests" -p no:warnings
```
To run the tests with coverage:
```bash
docker-compose exec api python -m pytest "src/tests" -p no:warnings --cov="src"
```
To run the tests with coverage:
```bash
docker-compose exec api python -m pytest "src/tests" -p no:warnings --cov="src"
```
To run the tests with coverage and generate an HTML report of the results:
```bash
docker-compose exec api python -m pytest "src/tests" -p no:warnings --cov="src" --cov-report html
```

## Tech Stack

**Server-Side:**
Python
Flask,
Flask-RESTx,
Flask-SQLAlchemy,
Flask-Admin,
SQLAlchemy,
Werkzeug

**Database:** PostgreSQL

**Testing and Development:**
Pytest,
Pytest-cov,
Pytest-xdist,
Black,
Flake8,
Isort

**Docker:**
Docker,
Docker Compose

**Version Control:**
Git,
GitLab

**Continuous Integration/Continuous Deployment (CI/CD):**
GitLab CI/CD

**Additional Tools:**
Gunicorn,
Psycopg2-binary,
Werkzeug middleware ProxyFix


## Features

- Return all users
- Creates a new user
- Updates a user 
- Delete a user

