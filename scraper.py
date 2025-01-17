from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from pymongo import MongoClient
from datetime import datetime
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time
import traceback

# MongoDB connection
client = MongoClient("mongodb+srv://revanasidda27792:4KiN1tANhxnMyXTg@cluster0.ul7jm.mongodb.net/?retryWrites=true&w=majority&appName=Cluster0")
db = client['twitter_scraper']
collection = db['trending_topics']

def scrape_x():
    # Initialize top_trends as an empty list
    top_trends = []
    
    # Set up Chrome options for headless browsing
    chrome_options = Options()
    chrome_options.add_argument("--no-sandbox")
    chrome_options.add_argument("--disable-dev-shm-usage")
    chrome_options.add_argument("--headless")  # Uncomment for headless mode
    
    # Path to chromedriver (ensure chromedriver is downloaded and in the correct path)
    chromedriver_path = r"chromedriver.exe"
    driver = webdriver.Chrome(service=Service(chromedriver_path), options=chrome_options)
    
    # Open X login page
    driver.get("https://x.com/login")
    print("Login page loaded...")
    
    try:
        # Wait for the username input field to be visible and enter the credentials
        username_input = WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.NAME, "text"))
        )
        username_input.send_keys("RevanasiddaNK")  # Replace with your X username
        driver.find_element(By.XPATH, '//span[text()="Next"]').click()
        
        # Wait for password input field to appear and enter the password
        password_input = WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.NAME, "password"))
        )
        password_input.send_keys("1nt22AI043")  # Replace with your X password
        driver.find_element(By.XPATH, '//span[text()="Log in"]').click()
        
        # Wait for login to complete
        WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.XPATH, '//div[@aria-label="Timeline: Your Home Timeline"]'))
        )
        print("Logged in successfully...")
    except Exception as e:
        driver.quit()
        print(f"Error during login: {e}")
        return top_trends  # Return empty list if login fails
    
    # Go to the X trending page
    driver.get("https://x.com/explore/tabs/trending")
    print("Navigated to X trending page...")
    
    try:
        # Increase the wait time for dynamic content to load
        print("Waiting for trends to load...")
        WebDriverWait(driver, 60).until(
            EC.presence_of_all_elements_located((By.XPATH, '//div[@data-testid="trend"]'))
        )
        print("Trends elements loaded successfully.")
        
        # Verify the number of trend elements found
        trends_elements = driver.find_elements(By.XPATH, '//div[@data-testid="trend"]')
        print(f"Trends elements found: {len(trends_elements)}")

        if trends_elements:
            # Collect top 5 trending topics
            top_trends = [trend.text for trend in trends_elements[:5]]
            print(f"Top 5 Trends: {top_trends}")
        else:
            print("No trends found.")

        # Prepare data to insert into MongoDB
        record = {
            "unique_id": str(datetime.now().timestamp()),
            "trend1": top_trends[0] if len(top_trends) > 0 else "",
            "trend2": top_trends[1] if len(top_trends) > 1 else "",
            "trend3": top_trends[2] if len(top_trends) > 2 else "",
            "trend4": top_trends[3] if len(top_trends) > 3 else "",
            "trend5": top_trends[4] if len(top_trends) > 4 else "",
            "datetime": datetime.now()
        }
        
        # Insert the data into MongoDB collection
        collection.insert_one(record)
        print("Data inserted into MongoDB successfully.")
        
    except Exception as e:
        print(f"Error fetching trends: {str(e)}")
        traceback.print_exc()
    finally:
        # Close the browser after scraping
        driver.quit()
    
    return top_trends  # Return the top trends

# You can call this function to scrape data
if __name__ == "__main__":
    trends = scrape_x()
    print("Final Trends:", trends)
