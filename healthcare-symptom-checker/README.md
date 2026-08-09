# AI-Based Healthcare Symptom Checker

A Django-based educational symptom-checking application with structured symptom capture and persistent interaction history.

## Features
- Symptom submission through a REST-style JSON endpoint
- Database-backed interaction history
- Simple rule-based guidance layer
- Django ORM models and migrations

## Run
```bash
cd healthcare-symptom-checker
python -m venv .venv
# Windows: .venv\Scripts\activate
pip install -r requirements.txt
python manage.py migrate
python manage.py runserver
```

API: `POST /api/check/` and `GET /api/history/`.

**Disclaimer:** This is an educational software project and does not provide medical diagnosis or replace a qualified healthcare professional.
