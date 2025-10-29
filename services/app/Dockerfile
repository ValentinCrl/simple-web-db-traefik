# Simple Flask app
FROM python:3.12-slim AS app

# Avoid python buffering
ENV PYTHONUNBUFFERED=1

WORKDIR /app

COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

COPY app.py .

EXPOSE 8000

# gunicorn is production-grade; bind to 0.0.0.0:8000
CMD ["gunicorn", "--bind", "0.0.0.0:8000", "app:app"]
