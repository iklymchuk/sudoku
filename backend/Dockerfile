# Backend Dockerfile
FROM python:3.12-slim

WORKDIR /app

# Copy requirements first to leverage Docker cache
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Copy the rest of the application
COPY . .

# Expose the port the app runs on
EXPOSE 8900

# Run the app as a module so package-relative imports work inside the container
CMD ["python", "-m", "app.main"]