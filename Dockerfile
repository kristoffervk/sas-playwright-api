FROM python:3.11-slim

# Install dependencies
RUN apt-get update && apt-get install -y \
    wget curl unzip fonts-liberation libx11-xcb1 libnss3 libxcomposite1 libxdamage1 \
    libxrandr2 libasound2 libatk1.0-0 libatk-bridge2.0-0 libcups2 \
    libgtk-3-0 libxss1 libxtst6 libx11-6 libxext6 libgbm1 \
    && apt-get clean

# Install Python packages
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Install Playwright and browser binaries
RUN python -m playwright install --with-deps chromium

# Add code
COPY . /app
WORKDIR /app

# Expose port
EXPOSE 8000

# Run the app
CMD ["python", "app.py"]
