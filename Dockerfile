FROM python:3.11-slim

WORKDIR /api

COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt
ENV PYTHONPATH=/api/webhook/app:/api/storage/app

COPY apis/ .
# COPY apis/streaming/ ./streaming/

COPY .env .env
COPY schema.sql .

EXPOSE 9999

COPY start.sh /start.sh
RUN chmod +x /start.sh
CMD ["/start.sh"]