FROM python:3.11-slim

WORKDIR /api

COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt
ENV PYTHONPATH=/api/webhook/app
ENV PYTHONPATH=/api/storage/app


COPY webhook/ ./webhook/
COPY streaming/ ./streaming/
COPY storage/ ./storage/

EXPOSE 9999

COPY start.sh /start.sh
RUN chmod +x /start.sh
CMD ["/start.sh"]