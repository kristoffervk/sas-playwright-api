FROM python:3.11-slim

# Install system dependencies
RUN apt-get update && apt-get install -y \
    curl wget gnupg ca-certificates fonts-liberation libnss3 libxss1 \
    libasound2 libatk1.0-0 libatk-bridge2.0-0 libcups2 libdrm2 libxcomposite1 \
    libxdamage1 libxrandr2 libgtk-3-0 libgbm1 libx11-xcb1 xdg-utils \
    && apt-get clean

# Install Python deps
WORKDIR /app
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt
RUN python -m playwright install chromium

# Copy code
COPY app.py .

# Expose Flask app
ENV FLASK_APP=app.py
CMD ["flask", "run", "--host=0.0.0.0", "--port=8000"]
