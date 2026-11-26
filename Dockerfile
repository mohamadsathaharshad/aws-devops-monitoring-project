# Python base image
FROM python:3.12-slim

# Working directory
WORKDIR /app

# Copy requirements
COPY requirements.txt .

# Install dependencies
RUN pip install --no-cache-dir -r requirements.txt

# Copy application files
COPY app/ ./app/

# Application port
EXPOSE 5000

# Start Flask application
CMD ["python", "app/app.py"]
