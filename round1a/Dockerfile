
FROM --platform=linux/amd64 python:3.10-slim

WORKDIR /app
COPY . /app

RUN apt-get update && apt-get install -y \
    tesseract-ocr poppler-utils libglib2.0-0 libsm6 libxext6 libxrender-dev \
    && rm -rf /var/lib/apt/lists/*
RUN pip install --no-cache-dir PyMuPDF pdfplumber opencv-python-headless pillow

CMD ["python", "main.py"]
