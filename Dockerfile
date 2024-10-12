# Stage 1: Build dependencies
FROM python:3.12-slim AS builder

# Use the current directory as the working directory
WORKDIR .

# Copy only requirements to cache dependencies
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Stage 2: Final image
FROM python:3.12-slim

# Use the current directory as the working directory
WORKDIR .

# Copy installed dependencies from the builder (including binaries)
COPY --from=builder /usr/local/lib/python3.12/site-packages /usr/local/lib/python3.12/site-packages
COPY --from=builder /usr/local/bin /usr/local/bin

# Copy the entire application to the current working directory
COPY . .

# Expose the default FastAPI port
EXPOSE 8000

# Run the FastAPI application with Uvicorn (updated path)
CMD ["uvicorn", "src.main:app", "--host", "0.0.0.0", "--port", "8000"]