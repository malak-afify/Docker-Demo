FROM python:3.10-slim AS builder

WORKDIR /app
RUN apt-get update && apt-get install -y --no-install-recommends gcc

COPY requirements.txt .
RUN pip install --no-cache-dir --target=/install -r requirements.txt


FROM python:3.10-slim AS runner

WORKDIR /app

COPY --from=builder /install /usr/local/lib/python3.10/site-packages

COPY . .

EXPOSE 5000

CMD ["python", "app.py"]
