FROM python:3.12-slim

WORKDIR /app

# Install system dependencies (needed for lxml/docx)
RUN apt-get update && apt-get install -y \
    build-essential \
    libxml2 \
    libxslt1.1 \
    libxml2-dev \
    libxslt1-dev \
    && rm -rf /var/lib/apt/lists/*

# Copy requirements first (for caching)
COPY requirements.txt .

RUN pip install --upgrade pip
RUN pip install -r requirements.txt

# Copy project files
COPY . .

# Render uses PORT env variable
CMD ["uvicorn", "app:app", "--host", "0.0.0.0", "--port", "10000"]