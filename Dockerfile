FROM python:3.13-bookworm

WORKDIR /app

ENV PYTHONPATH=/app

COPY requirements.txt .

RUN pip install --no-cache-dir -r requirements.txt

COPY app/. .
COPY .env .

RUN chmod +x prestart.sh

ENTRYPOINT ["sh", "./prestart.sh"]
CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "8000"]