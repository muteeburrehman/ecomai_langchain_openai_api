FROM python:3.11-slim

WORKDIR /app

COPY requirements.txt .

# Upgrade pip first
RUN pip install --upgrade pip

# Install with timeout + retry
RUN pip install --default-timeout=120 --no-cache-dir -r requirements.txt

COPY . .

CMD ["uvicorn", "app.main:app", "--host", "0.0.0.0", "--port", "8000"]
