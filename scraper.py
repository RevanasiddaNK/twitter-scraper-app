import os
import logging
import traceback
from datetime import datetime
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from webdriver_manager.chrome import ChromeDriverManager  # Automatically manages ChromeDriver
from pymongo import MongoClient
from dotenv import load_dotenv

# Load environment variables
load_dotenv()

# Configure logging
logging.basicConfig(level=logging.INFO, format="%(asctime)s - %(levelname)s - %(message)s")

# MongoDB connection
mongo_uri = os.getenv("MONGO_URI")
client = MongoClient(mongo_uri)
db = client['twitter_scraper']
collection = db['trending_topics']

def scrape_x():
    """
    Scrapes trending topics from the 'X' platform and stores them in MongoDB.
    """
    logging.info("Starting the scraping process...")

    # Initialize variables
    top_trends = []

    # Set Chrome options
    chrome_options = Options()
    chrome_options.add_argument("--no-sandbox")
    chrome_options.add_argument("--disable-dev-shm-usage")
    chrome_options.add_argument("--headless")
    chrome_options.add_argument("--disable-gpu")  # Prevents rendering issues on some hosts
    
    # Specify the path to the Chrome binary
    chrome_binary_path = "/usr/bin/google-chrome"  # Adjust for your system
    chrome_options.binary_location = chrome_binary_path

    try:
        # Automatically download and configure ChromeDriver
        driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=chrome_options)
        logging.info("WebDriver initialized successfully.")
    except Exception as e:
        logging.error(f"Error initializing WebDriver: {str(e)}")
        traceback.print_exc()
        return

    try:
        # Login process
        driver.get("https://x.com/login")
        logging.info("Navigated to login page.")

        # Enter username
        username_input = WebDriverWait(driver, 15).until(
            EC.presence_of_element_located((By.NAME, "text"))
        )
        username_input.send_keys(os.getenv("X_USERNAME"))
        driver.find_element(By.XPATH, '//span[text()="Next"]').click()
        logging.info("Entered username and clicked Next.")

        # Enter password
        password_input = WebDriverWait(driver, 15).until(
            EC.presence_of_element_located((By.NAME, "password"))
        )
        password_input.send_keys(os.getenv("X_PASSWORD"))
        driver.find_element(By.XPATH, '//span[text()="Log in"]').click()
        logging.info("Entered password and clicked Log in.")

        # Wait for the home timeline to load
        WebDriverWait(driver, 30).until(
            EC.presence_of_element_located((By.XPATH, '//div[@aria-label="Timeline: Your Home Timeline"]'))
        )
        logging.info("Successfully logged in and home timeline loaded.")

        # Navigate to trending topics
        driver.get("https://x.com/explore/tabs/trending")
        WebDriverWait(driver, 30).until(
            EC.presence_of_all_elements_located((By.XPATH, '//div[@data-testid="trend"]'))
        )
        logging.info("Navigated to trending topics page.")

        # Extract trending topics
        trends_elements = driver.find_elements(By.XPATH, '//div[@data-testid="trend"]')
        top_trends = [trend.text for trend in trends_elements[:5]]
        logging.info(f"Extracted trends: {top_trends}")

        # Save trends to MongoDB
        record = {
            "unique_id": str(datetime.now().timestamp()),
            "trends": top_trends,
            "datetime": datetime.now()
        }
        collection.insert_one(record)
        logging.info("Saved trends to MongoDB.")

    except Exception as e:
        logging.error(f"Error during scraping: {str(e)}")
        traceback.print_exc()
    finally:
        driver.quit()
        logging.info("Closed WebDriver.")

    return top_trends
