FROM python:3.11-slim

# Install system dependencies for Chromium
RUN apt-get update && apt-get install -y \
    wget curl gnupg ca-certificates fonts-liberation libnss3 libxss1 \
    libasound2 libatk1.0-0 libatk-bridge2.0-0 libcups2 libdrm2 libxcomposite1 \
    libxdamage1 libxrandr2 libgtk-3-0 libgbm1 libx11-xcb1 xdg-utils \
    && apt-get clean

# Set up working directory
WORKDIR /app

# Install Python dependencies
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt
RUN python -m playwright install chromium

# Copy app code
COPY app.py .

# Expose port (optional, for clarity)
EXPOSE 8000

# Run app
CMD ["python", "app.py"]
