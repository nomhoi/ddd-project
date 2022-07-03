FROM python:3.10-slim-buster

COPY requirements.txt /tmp/
RUN pip install -r /tmp/requirements.txt

RUN mkdir -p /src
COPY src/ /src/
COPY tests/ /tests/

WORKDIR /src

CMD ["uvicorn", "application.entrypoints.main:app", "--host", "0.0.0.0", "--port", "8000"]
