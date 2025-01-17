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

app = Flask(__name__)

# MongoDB connection URI
mongo_uri = os.getenv("MONGO_URI")
client = MongoClient(mongo_uri)
db = client['twitter_scraper']
collection = db['trending_topics']

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/run-scraper', methods=['GET'])
def run_scraper():
    try:
        result = scrape_x()
        return jsonify({"message": "Scraping complete", "data": result}), 200
    except Exception as e:
        app.logger.error(f"Error in running scraper: {str(e)}")
        return jsonify({"message": "Error during scraping", "error": str(e)}), 500

@app.route('/get-trends', methods=['GET'])
def get_trends():
    try:
        records = list(collection.find().sort("datetime", -1).limit(1))
        def serialize_document(doc):
            doc['_id'] = str(doc['_id'])
            return doc

        serialized_records = [serialize_document(record) for record in records]
        return jsonify(serialized_records), 200
    except Exception as e:
        app.logger.error(f"Error in fetching trends: {str(e)}")
        return jsonify({"message": "Error fetching trends", "error": str(e)}), 500

if __name__ == "__main__":
    app.run(debug=True)
