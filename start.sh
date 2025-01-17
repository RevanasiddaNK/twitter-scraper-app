# start.sh
apt-get update
apt-get install -y wget gnupg2 curl
curl -sSL https://dl.google.com/linux/direct/google-chrome-stable_current_amd64.deb -o google-chrome.deb
dpkg -i google-chrome.deb
apt-get -f install  # Fix missing dependencies

# Now run the Python script
python3 scraper.py
