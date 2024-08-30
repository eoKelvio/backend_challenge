FROM python:3.11-slim

WORKDIR /api

COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt
ENV PYTHONPATH=/api/webhook/app


COPY webhook/ ./webhook/
COPY streaming/ ./streaming/
COPY storage/ ./storage/

EXPOSE 9999

CMD ["uvicorn", "webhook.app.main:app", "--host", "0.0.0.0", "--port", "9999", "--reload"]