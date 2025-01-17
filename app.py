import os
from flask import Flask, render_template, jsonify
from scraper import scrape_x  # Ensure you're importing the correct function
from pymongo import MongoClient
from bson import ObjectId
from datetime import datetime
from dotenv import load_dotenv  # Import dotenv to load .env file
import logging
from logging.handlers import RotatingFileHandler

# Load environment variables
load_dotenv()

# Initialize Flask app
app = Flask(__name__)

# MongoDB connection URI
mongo_uri = os.getenv("MONGO_URI")
client = MongoClient(mongo_uri)
db = client['twitter_scraper']
collection = db['trending_topics']

# Logging configuration
log_file = "app.log"
logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s - %(levelname)s - %(message)s",
    handlers=[
        RotatingFileHandler(log_file, maxBytes=10 * 1024 * 1024, backupCount=5),  # Log rotation
        logging.StreamHandler()  # Console logging
    ]
)
logger = logging.getLogger(__name__)

@app.route('/')
def index():
    """Render the home page."""
    return render_template('index.html')

@app.route('/run-scraper', methods=['GET'])
def run_scraper():
    """
    Run the scraper and return the scraped data.
    """
    try:
        result = scrape_x()
        return jsonify({"message": "Scraping complete", "data": result}), 200
    except Exception as e:
        logger.error(f"Error in running scraper: {str(e)}")
        return jsonify({"message": "Error during scraping", "error": str(e)}), 500

@app.route('/get-trends', methods=['GET'])
def get_trends():
    """
    Fetch the latest trends from MongoDB.
    """
    try:
        # Fetch the latest record
        records = list(collection.find().sort("datetime", -1).limit(1))

        def serialize_document(doc):
            """Convert MongoDB ObjectId to string for JSON serialization."""
            doc['_id'] = str(doc['_id'])
            return doc

        serialized_records = [serialize_document(record) for record in records]
        return jsonify(serialized_records), 200
    except Exception as e:
        logger.error(f"Error in fetching trends: {str(e)}")
        return jsonify({"message": "Error fetching trends", "error": str(e)}), 500

if __name__ == "__main__":
    # Check for production environment
    is_production = os.getenv("FLASK_ENV") == "production"

    if is_production:
        # Configure for production
        from waitress import serve
        logger.info("Starting application in production mode with Waitress.")
        serve(app, host="0.0.0.0", port=int(os.getenv("PORT", 5000)))
    else:
        # Development mode
        logger.info("Starting application in development mode.")
        app.run(debug=True, host="0.0.0.0", port=int(os.getenv("PORT", 5000)))
