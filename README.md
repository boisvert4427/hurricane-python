# Hurricane Python

Base de projet API avec Flask, organisee par couches simples.

## Structure

```text
app/
  api/
    routes/
  models/
  repositories/
  schemas/
  services/
tests/
run.py
requirements.txt
```

## Installation

```bash
source .venv/bin/activate
pip install -r requirements-dev.txt
```

## Lancer l'API

```bash
python run.py
```

## Endpoints

- `GET /`
- `GET /api/v1/health`
- `GET /api/v1/objects`
- `GET /api/v1/objects/<object_id>`
- `POST /api/v1/objects`
