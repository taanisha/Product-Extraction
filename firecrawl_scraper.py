import os
import requests
from dotenv import load_dotenv


load_dotenv()
FIRECRAWL_API_KEY=os.getenv("FIRECRAWL_API_KEY")

def scrape_with_firecrawl(url:str):
    if not url:
        return {"error": "URL is empty."}
    print(f"Scraping URL: {url}")
    headers={
        "Authorization":f"Bearer {FIRECRAWL_API_KEY}",
        "Content-type":"application/json"
    }
    payload={
        "url":url,
        "formats": ["markdown"]
        
    }
    
    response=requests.post("https://api.firecrawl.dev/v1/scrape", headers=headers, json=payload)
    # Check for the raw response data
    print(f"Response Status Code: {response.status_code}")
    print(f"Response Text: {response.text}")
    if response.status_code==200:
        return response.text
    else:
        raise Exception(f"Firecrawl error: {response.status_code} - {response.text}")






url="https://www.bluelettuce.in/our-products/"
d=scrape_with_firecrawl(url)
print(d)