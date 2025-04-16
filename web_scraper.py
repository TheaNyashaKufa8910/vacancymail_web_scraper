import requests
from bs4 import BeautifulSoup
import pandas as pd
from datetime import datetime
import logging
import os

# Create logs directory
os.makedirs("logs", exist_ok=True)

# Set up logging
logging.basicConfig(
    filename="logs/scraper.log",
    level=logging.INFO,
    format="%(asctime)s - %(levelname)s - %(message)s"
)

def scrape_jobs():
    url = "https://vacancymail.co.zw/jobs/"
    headers = {
        'User-Agent': 'Mozilla/5.0'
    }

    try:
        response = requests.get(url, headers=headers)
        response.raise_for_status()
        soup = BeautifulSoup(response.text, 'html.parser')

        job_cards = soup.find_all('a', class_='job-listing')[:10]
        logging.info(f"Found {len(job_cards)} job cards.")

        jobs = []
        for card in job_cards:
            try:
                title = card.find('h3', class_='job-listing-title').get_text(strip=True)
                desc = card.find('p', class_='job-listing-text').get_text(strip=True)
                link = "https://vacancymail.co.zw" + card['href']

                # Try to extract details inside the <ul> list
                detail_items = card.find_all('li')
                location = expiry_date = company = "Not specified"

                for item in detail_items:
                    text = item.get_text(strip=True)
                    if "Location:" in text:
                        location = text.replace("Location:", "").strip()
                    elif "Expires" in text:
                        expiry_date = text.replace("Expires", "").strip()
                    elif "Company:" in text:
                        company = text.replace("Company:", "").strip()

                jobs.append({
                    "Job Title": title,
                    "Company": company,
                    "Location": location,
                    "Expiry Date": expiry_date,
                    "Description": desc,
                    "Link": link
                })

            except Exception as e:
                logging.warning(f"Error processing a job card: {e}")
                continue

        # Convert to DataFrame and clean
        df = pd.DataFrame(jobs)
        df.drop_duplicates(inplace=True)

        filename = f"scraped_data_{datetime.now().strftime('%Y%m%d_%H%M%S')}.csv"
        df.to_csv(filename, index=False)

        logging.info(f"Scraped {len(df)} jobs. Data saved to {filename}")
        print(f"Scraped {len(df)} jobs to {filename}")

    except requests.RequestException as e:
        logging.error(f"Network error: {e}")
        print("Failed to fetch jobs due to a network error.")
    except Exception as e:
        logging.error(f"Unexpected error: {e}")
        print("An unexpected error occurred.")

if __name__ == "__main__":
    scrape_jobs()

import schedule
import time

def job():
    scrape_jobs()  # Calls the function to scrape jobs

# Schedule the job to run daily at 10 AM
schedule.every().day.at("10:00").do(job)

# Infinite loop to keep the script running and check the schedule
while True:
    schedule.run_pending()
    time.sleep(60)  # Check every minute


