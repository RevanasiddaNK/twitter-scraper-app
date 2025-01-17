import os
from flask import Flask, render_template, jsonify
from scraper import scrape_x  # Ensure you're importing the correct function
from pymongo import MongoClient
from bson import ObjectId  # Import to handle ObjectId serialization
from datetime import datetime
import logging
from logging.handlers import RotatingFileHandler

app = Flask(__name__)

# MongoDB connection URI (use environment variable for production)
mongo_uri = os.getenv("MONGO_URI", "mongodb+srv://revanasidda27792:4KiN1tANhxnMyXTg@cluster0.ul7jm.mongodb.net/?retryWrites=true&w=majority&appName=Cluster0")
client = MongoClient(mongo_uri)
db = client['twitter_scraper']
collection = db['trending_topics']

@app.route('/')
def index():
    # Render the index page (ensure you have the 'index.html' file in your templates folder)
    return render_template('index.html')

@app.route('/run-scraper', methods=['GET'])
def run_scraper():
    # Call the Twitter scraper function to scrape the top 5 trends
    try:
        result = scrape_x()  # Ensure the scrape_x function works as expected
        return jsonify({"message": "Scraping complete", "data": result}), 200
    except Exception as e:
        app.logger.error(f"Error in running scraper: {str(e)}")
        return jsonify({"message": "Error during scraping", "error": str(e)}), 500

@app.route('/get-trends', methods=['GET'])
def get_trends():
    # Fetch the most recent trends from the database
    try:
        records = list(collection.find().sort("datetime", -1).limit(1))
        
        # Convert ObjectId and other non-serializable fields to a JSON serializable format
        def serialize_document(doc):
            doc['_id'] = str(doc['_id'])  # Convert ObjectId to string
            return doc

        # Serialize all records (if any)
        serialized_records = [serialize_document(record) for record in records]
        return jsonify(serialized_records), 200
    except Exception as e:
        app.logger.error(f"Error in fetching trends: {str(e)}")
        return jsonify({"message": "Error fetching trends", "error": str(e)}), 500

if __name__ == "__main__":
    app.run(debug=True)