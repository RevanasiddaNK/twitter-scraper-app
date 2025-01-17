# Twitter Scraper Flask App

This is a simple and user-friendly web application built with Flask. It scrapes trending topics from Twitter (X) using Selenium and stores the data in a MongoDB database. The app provides an intuitive interface to initiate the scraping process and view the latest trends.

---

## Features

- **Scrape Trending Topics:** Automatically scrape the latest trending topics from Twitter (X) using Selenium.
- **Data Storage:** Store scraped data securely in a MongoDB database for easy access and analysis.
- **Interactive Web Interface:** Use the web interface to control the scraper and view the latest trends in real time.

---

## Project Structure

```plaintext
.
├── app.py           # Main Flask application
├── scraper.py       # Selenium-based scraper for Twitter (X)
├── templates/       # Directory for HTML templates
│   └── index.html   # Main HTML page for the web interface
├── chromedriver.exe # ChromeDriver executable for Selenium
├── requirements.txt # Python dependencies
└── README.md        # Project documentation
```

---

## Prerequisites

Before running the application, ensure you have the following installed:

1. **Python 3.8+**
2. **Google Chrome** (compatible version with your ChromeDriver)
3. **MongoDB** (running locally or remotely)
4. **ChromeDriver** (download the version matching your Chrome installation)

---

## Installation

1. Clone this repository:
   ```bash
   git clone https://github.com/yourusername/twitter-scraper-flask-app.git
   cd twitter-scraper-flask-app
   ```

2. Create and activate a virtual environment:
   ```bash
   python -m venv venv
   source venv/bin/activate   # On Windows: venv\Scripts\activate
   ```

3. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```

4. Set up MongoDB:
   - Ensure MongoDB is running locally or update the connection string in `app.py` to point to your remote MongoDB instance.

5. Update `chromedriver.exe`:
   - Replace `chromedriver.exe` with the version compatible with your Google Chrome browser.

---

## Usage

1. Start the Flask application:
   ```bash
   python app.py
   ```

2. Open your web browser and navigate to:
   ```plaintext
   http://127.0.0.1:5000/
   ```

3. Use the web interface to:
   - Run the scraper and fetch trending topics.
   - View the latest scraped data.

---

## File Descriptions

- **`app.py`**
  - Contains the Flask application logic.
  - Routes for running the scraper and displaying data.

- **`scraper.py`**
  - Implements the Selenium-based scraper to extract trending topics from Twitter (X).

- **`templates/index.html`**
  - HTML page that serves as the front-end interface for the application.

- **`chromedriver.exe`**
  - ChromeDriver executable required by Selenium to automate Chrome.

- **`requirements.txt`**
  - List of Python dependencies required for the application.

---

## Dependencies

Install the dependencies using the `requirements.txt` file:

```bash
pip install -r requirements.txt
```

Key dependencies include:

- **Flask**: Web framework for building the application.
- **Selenium**: Automates the web scraping process.
- **pymongo**: Connects to MongoDB for data storage.
- **BeautifulSoup** (optional): Parses HTML for additional data extraction (if required).

---

## Troubleshooting

- **ChromeDriver Version Mismatch:**
  - Ensure that `chromedriver.exe` matches the version of your Google Chrome browser.

- **MongoDB Connection Issues:**
  - Verify that MongoDB is running and accessible at the specified connection string in `app.py`.

- **Selenium Errors:**
  - Update your Selenium and ChromeDriver versions to the latest compatible versions.

---

## Future Enhancements

- Add user authentication for secure access.
- Enhance the scraper to include additional data (e.g., hashtags, tweet counts).
- Implement error handling and logging for better debugging.
- Deploy the application using Docker for improved portability.

---

## License

This project is licensed under the [MIT License](LICENSE).

---

## Contributions

Contributions are welcome! Feel free to fork the repository and submit a pull request.

For major changes, please open an issue first to discuss what you would like to change.

---

## Acknowledgments

- **Flask Documentation:** [https://flask.palletsprojects.com/](https://flask.palletsprojects.com/)
- **Selenium Documentation:** [https://www.selenium.dev/documentation/](https://www.selenium.dev/documentation/)
- **MongoDB Documentation:** [https://www.mongodb.com/docs/](https://www.mongodb.com/docs/)

---

Thank you for using the Twitter Scraper Flask App! Feel free to provide feedback or report issues to improve the project.

