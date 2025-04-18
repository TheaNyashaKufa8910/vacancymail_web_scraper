# Job Scraper - VacancyMail Zimbabwe

This Python script scrapes the **10 most recent job listings** from [VacancyMail Zimbabwe](https://vacancymail.co.zw/jobs/), extracts key details, and saves the data to a structured CSV file. It includes logging, error handling, and optional scheduling using the `schedule` library.

## 📌 Features

- Scrapes job title, company, location, expiry date, description, and job link.
- Stores data in a clean CSV format.
- Removes duplicate entries.
- Logs all scraping activity and errors.
- Optionally runs automatically at scheduled times.


## Requirements

Install the required libraries using:

pip install -r requirements.txt


**requirements.txt:**

requests
beautifulsoup4
pandas
schedule

## 🚀 Usage

### 🔹 To Run the Scraper Manually


python web_scraper.py


A CSV file will be generated with the filename format:

scraped_data_YYYYMMDD_HHMMSS.csv


### 🔹 Optional: Schedule the Scraper

You can set the script to run automatically using the `schedule` module.

#### Example (in `web_scraper.py`):
python
import schedule
import time
def job():
    scrape_jobs()

# Run every day at 10:00 AM
schedule.every().day.at("10:00").do(job)
while True:
    schedule.run_pending()
    time.sleep(60)

> Keep this script running in the background or set it up with a task scheduler (`cron`, `Task Scheduler`, etc.) for automation.



## 📝 Output

The output CSV will include:
- Job Title
- Company
- Location
- Expiry Date
- Description
- Link



## 📂 Logs

All activity and errors are recorded in:

logs/scraper.log

This helps with debugging or checking what happened during each run.



## 📎 Notes

- Make sure you’re connected to the internet before running the scraper.
- If the website’s structure changes, the script may need updates to keep working.
- Tested with Python 3.10+.



## 🧠 Credits
Made with 💙 by Nyasha Thea Kufa 


 ## License
This project is open-source and free to use under the MIT License.
#   v a c a n c y m a i l _ w e b _ s c r a p e r  
 