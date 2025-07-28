
FROM --platform=linux/amd64 python:3.10-slim

WORKDIR /app
COPY . /app

RUN apt-get update && apt-get install -y libglib2.0-0 libsm6 libxext6 libxrender-dev && rm -rf /var/lib/apt/lists/*
RUN pip install --no-cache-dir sentence-transformers PyMuPDF scikit-learn numpy

COPY model /app/model

CMD ["python", "main.py"]
