import os
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from pymongo import MongoClient
from datetime import datetime
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from dotenv import load_dotenv  # Import dotenv to load .env file
import time
import traceback

# Load environment variables
load_dotenv()

# MongoDB connection
mongo_uri = os.getenv("MONGO_URI")
client = MongoClient(mongo_uri)
db = client['twitter_scraper']
collection = db['trending_topics']

def scrape_x():
    top_trends = []
    chrome_options = Options()
    chrome_options.add_argument("--no-sandbox")
    chrome_options.add_argument("--disable-dev-shm-usage")
    chrome_options.add_argument("--headless")

    chromedriver_path = os.getenv("CHROMEDRIVER_PATH")
    driver = webdriver.Chrome(service=Service(chromedriver_path), options=chrome_options)

    try:
        driver.get("https://x.com/login")
        username_input = WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.NAME, "text"))
        )
        username_input.send_keys(os.getenv("X_USERNAME"))
        driver.find_element(By.XPATH, '//span[text()="Next"]').click()

        password_input = WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.NAME, "password"))
        )
        password_input.send_keys(os.getenv("X_PASSWORD"))
        driver.find_element(By.XPATH, '//span[text()="Log in"]').click()

        WebDriverWait(driver, 300).until(
            EC.presence_of_element_located((By.XPATH, '//div[@aria-label="Timeline: Your Home Timeline"]'))
        )

        driver.get("https://x.com/explore/tabs/trending")
        WebDriverWait(driver, 300).until(
            EC.presence_of_all_elements_located((By.XPATH, '//div[@data-testid="trend"]'))
        )

        trends_elements = driver.find_elements(By.XPATH, '//div[@data-testid="trend"]')
        top_trends = [trend.text for trend in trends_elements[:5]]

        record = {
            "unique_id": str(datetime.now().timestamp()),
            "trend1": top_trends[0] if len(top_trends) > 0 else "",
            "trend2": top_trends[1] if len(top_trends) > 1 else "",
            "trend3": top_trends[2] if len(top_trends) > 2 else "",
            "trend4": top_trends[3] if len(top_trends) > 3 else "",
            "trend5": top_trends[4] if len(top_trends) > 4 else "",
            "datetime": datetime.now()
        }

        collection.insert_one(record)
    except Exception as e:
        print(f"Error fetching trends: {str(e)}")
        traceback.print_exc()
    finally:
        driver.quit()

    return top_trends
