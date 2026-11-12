from pathlib import Path
import pandas as pd
import requests
from bs4 import BeautifulSoup


def scrape_web(website_url: str, output_csv: str) -> None:
    """
    Scrape fake python job listings.

    PARAMETERS:
        website_url: URL of website.
        output_csv: Output path of csv.
    """
    try:
        page = requests.get(website_url, timeout=10)
        page.raise_for_status()
        soup = BeautifulSoup(page.content, "html.parser")

        results = soup.find(id="ResultsContainer")
        job_cards = results.find_all("div", "card-content")
        jobs_list = []
        for job_card in job_cards:
            title = job_card.find("h2", "title").text.strip()
            company = job_card.find("h3", "subtitle is-6 company").text.strip()
            location = job_card.find("p", "location").text.strip()
            url = job_card.find("a", href=True)["href"]

            jobs_list.append({
                "job_title": title,
                "company": company,
                "location": location,
                "job_detail_url": url
            })
        jobs_df = pd.DataFrame(jobs_list)
        jobs_df.to_csv(output_csv)

    except requests.Timeout as timeoutE:
        raise SystemExit("Time respond to long:", timeoutE)
    except requests.HTTPError as httpE:
        raise SystemExit("HTTP Eror:", httpE)


if __name__ == "__main__":
    URL = "https://realpython.github.io/fake-jobs/"
    scrape_web(URL, "listing_jobs.csv")