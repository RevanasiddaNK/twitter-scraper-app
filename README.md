# Twitter Scraper App

This is a simple Flask-based web application that scrapes Twitter's (X) trending topics and stores them in a MongoDB database. It uses Selenium WebDriver with Chrome to navigate Twitter's login page, retrieve the top trending topics, and display them on a webpage.

---

## Features

- Scrapes Twitter's trending topics.
- Stores the top 5 trends in MongoDB.
- Displays the trends on a simple webpage.
- Allows users to trigger the scraper with a button.

---

## Prerequisites

- Python 3.7+
- Google Chrome (with ChromeDriver)
- MongoDB (use Atlas for a cloud database or set up locally)
- `chromedriver.exe` (ensure it is downloaded and compatible with your version of Chrome)

---

## How to Run the Project

### 1. Clone the Repository

Run the following command to clone this project:
```bash
git clone https://github.com/RevanasiddaNK/twitter-scraper-app.git
cd twitter-scraper-app
```

### 2. Install Required Dependencies

Navigate to the project directory and install the necessary Python packages:
```bash
pip install -r requirements.txt
```

### 3. Set Up MongoDB

- If using MongoDB Atlas, create a cluster and obtain the connection URI.
- If using a local MongoDB setup, ensure MongoDB is running.

Update the `mongo_uri` in `.env` to match your MongoDB connection string.

### 4. Download ChromeDriver

- Download the appropriate version of ChromeDriver for your system from: https://sites.google.com/a/chromium.org/chromedriver/
- Place `chromedriver.exe` in the project directory (or specify the correct path in `.env`).

### 5. Run the Flask App

Run the Flask server with the following command:
```bash
python app.py
```

The application will be accessible at `http://127.0.0.1:5000/`.

### 6. Trigger the Scraper

On the web page, click the button to trigger the scraper, which will fetch the latest trending topics and display them on the page.

---

## Folder Structure

```plaintext
twitter-scraper-app/
├── app.py                # Flask app
├── scraper.py            # Twitter scraper logic
├── templates/
│   └── index.html        # HTML template for displaying trends
├── chromedriver.exe      # Chrome WebDriver (make sure it's compatible with your version of Chrome)
├── requirements.txt      # Python dependencies
└── README.md             # Project documentation
└── .env 
```

---

## Dependencies

The following Python libraries are required:

- Flask
- selenium
- pymongo
- bson

You can install all dependencies by running:
```bash
pip install -r requirements.txt
```

---

## Environment Variables

Create a `.env` file in the root directory of the project with the following template:

```
MONGO_URI=mongodb+srv://<username>:<password>@cluster0.mongodb.net/<dbname>?retryWrites=true&w=majority&appName=Cluster0
X_USERNAME=<twitter_username>
X_PASSWORD=<twitter_password>
CHROMEDRIVER_PATH=chromedriver.exe
```

Replace `<username>`, `<password>`, `<dbname>`, `<twitter_username>`, and `<twitter_password>` with your MongoDB credentials and Twitter login details. Ensure the `CHROMEDRIVER_PATH` points to your `chromedriver.exe` file.

---

## Troubleshooting

- **ChromeDriver Version Mismatch:**
  Ensure `chromedriver.exe` matches the version of your Google Chrome browser. If you encounter issues with the driver, check for updates at https://sites.google.com/a/chromium.org/chromedriver/.

- **MongoDB Connection Issues:**
  Double-check your MongoDB URI and ensure the MongoDB service is running.

---
## Application Screenshot
![image](https://github.com/user-attachments/assets/b6948ed5-2d5b-49d8-8caa-791c7e9af2ad)





## License

This project is licensed under the MIT License.

---

## Contributions

Contributions are welcome! Feel free to fork the repository and submit a pull request.

For major changes, please open an issue first to discuss what you would like to change.

---

Thank you for using the Twitter Scraper App! Feel free to provide feedback or report issues to improve the project.

