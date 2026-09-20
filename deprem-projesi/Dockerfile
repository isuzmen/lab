FROM python:3.12-slim

WORKDIR /app
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt
COPY indir_ve_yaz.py .

WORKDIR /veri
CMD ["python", "/app/indir_ve_yaz.py"]
