# Use Python 3.12 Alpine as base image for a lightweight container
FROM python:3.12-alpine

# Set PYTHONUNBUFFERED to ensure Python output is sent straight to the terminal without buffering
# This is important for proper logging in containerized environments
ENV PYTHONUNBUFFERED=1

# Set working directory where the application will run
WORKDIR /app

# Copy and install requirements first to leverage Docker's caching mechanism
# This layer will only rebuild when requirements.txt changes
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Copy the rest of the application code
# This comes after dependencies to optimize build time when code changes but dependencies don't
COPY . .

# Document that the application listens on port 8000
EXPOSE 8000

# Run the FastAPI application using Uvicorn ASGI server
# Uvicorn is used instead of raw Python to provide:
# - Better performance (built on uvloop and httptools)
# - Production-ready features (signal handling, process management)
# - Native support for asynchronous code
# - Proper handling of FastAPI's ASGI interface
CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "8000"]