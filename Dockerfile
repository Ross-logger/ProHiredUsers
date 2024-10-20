# Stage 1: Build dependencies
FROM python:3.12-slim AS builder

WORKDIR app/

# Copy only requirements to cache dependencies
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

FROM python:3.12-slim

WORKDIR app/

# Copy installed dependencies from the builder (including binaries)
COPY --from=builder /usr/local/lib/python3.12/site-packages /usr/local/lib/python3.12/site-packages
COPY --from=builder /usr/local/bin /usr/local/bin

# Copy the entire application to the current working directory
COPY . .

EXPOSE 8000

CMD ["uvicorn", "src.main:app", "--host", "0.0.0.0", "--port", "8000"]