# FastAPI and PostgreSQL - Base DDD Project Generator

## Based on

https://github.com/cosmicpython/code
https://github.com/nightriddler/fastapi_realworld


## Features

* Full **Docker** integration (Docker based).
* **Docker Compose** integration and optimization for local development.
* **SQLAlchemy** models.
* **Alembic** migrations.
* **Poetry**.
* **Pytest**.


## How to use it

Go to the directory where you want to create your project and run:

```bash
pip install --user cookiecutter
cookiecutter https://github.com/nomhoi/ddd-project
```


## Setup Project

```
cd {{ project_slug }}
cp .env.example .env
echo SECRET=$(openssl rand -hex 32) >> .env
make build
make alembic-upgrade-head
make up
```

Go to http://localhost:8000/docs


## License

This project is licensed under the terms of the MIT license.
