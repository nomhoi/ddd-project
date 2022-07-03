# {{cookiecutter.project_name}}
This is a great README file by {{cookiecutter.author}} ({{cookiecutter.email}})

The project is about:
{{cookiecutter.description}}

# Setup Project

```
cp .env.example .env
echo SECRET=$(openssl rand -hex 32) >> .env
make build
make alembic-upgrade-head
make up
```

Go to http://localhost:8000/docs
