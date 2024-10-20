# Stage 1: Build dependencies
FROM python:3.12-slim AS builder

# Set the working directory inside the container to app/
WORKDIR /app/

# Copy only requirements.txt to cache dependencies
COPY requirements.txt .

# Install dependencies
RUN pip install --no-cache-dir -r requirements.txt

# Stage 2: Final image
FROM python:3.12-slim

# Set the working directory inside the container to app/
WORKDIR /app/

# Copy installed dependencies from the builder (including binaries)
COPY --from=builder /usr/local/lib/python3.12/site-packages /usr/local/lib/python3.12/site-packages
COPY --from=builder /usr/local/bin /usr/local/bin

# Copy the entire application to /app/ (current working directory)
COPY . .

# Expose port 8000
EXPOSE 8000

# Set the default command to run uvicorn
CMD ["uvicorn", "src.main:app", "--host", "0.0.0.0", "--port", "8000"]