# Use a Python base image (you can change this depending on your app's language)
FROM python:3.9-slim

# Install system dependencies and Chrome
RUN apt-get update && apt-get install -y \
    wget \
    gnupg2 \
    curl \
    unzip \
    lsb-release \
    libxss1 \
    libappindicator3-1 \
    libindicator7 \
    ca-certificates \
    fonts-liberation \
    libnss3 \
    libgdk-pixbuf2.0-0 \
    libx11-xcb1 \
    xdg-utils \
    --no-install-recommends \
    && rm -rf /var/lib/apt/lists/*

# Install Google Chrome
RUN curl -sSL https://dl.google.com/linux/direct/google-chrome-stable_current_amd64.deb -o google-chrome.deb
RUN dpkg -i google-chrome.deb || apt-get install -f -y

# Install ChromeDriver
RUN curl -sSL https://chromedriver.storage.googleapis.com/113.0.5672.63/chromedriver_linux64.zip -o chromedriver.zip
RUN unzip chromedriver.zip -d /usr/local/bin/
RUN chmod +x /usr/local/bin/chromedriver

# Install Python dependencies (you'll need to have a requirements.txt file)
COPY requirements.txt /app/
RUN pip install --no-cache-dir -r /app/requirements.txt

# Set the working directory to /app
WORKDIR /app

# Copy the rest of your application code
COPY . /app

# Install other Python dependencies if needed
RUN pip install selenium webdriver-manager

# Expose the required port (if your app listens on a port)
EXPOSE 5000

# Start the application
CMD ["python", "scraper.py"]
