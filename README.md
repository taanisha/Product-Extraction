# Product-Extraction
# Smart Crop Scraper

A smart AI-powered web tool that extracts structured product data (crop name and price per kg) from hydroponic e-commerce websites. Built using **Firecrawl** for web scraping and **Mistral via OpenRouter** for natural language parsing, all wrapped inside a user-friendly **Streamlit** app.

---

## 🚀 Features

- Accepts a public product URL (e.g., hydroponic crop store)
- Scrapes clean markdown text from the page using **Firecrawl API**
- Sends the text to a **LLM (Mistral)** through **OpenRouter**
- Extracts and displays structured product data in JSON format
- Simple and clean **Streamlit** UI

---

##  Sample Output Format

```json
[
  { "product": "Lettuce Butterhead", "price_per_kg": 160 },
  { "product": "Spinach Baby", "price_per_kg": 125 }
]

##Screenshots
![Screenshot 1](https://github.com/your-username/your-repo-name/raw/main/assets/Screenshot%202025-04-16%20162623.png)
![Screenshot 2](https://github.com/your-username/your-repo-name/raw/main/assets/Screenshot%202025-04-16%20162650.png)
![Screenshot 3](https://github.com/taanisha/Product-Extraction/blob/main/Screenshot%202025-04-16%20163259.png)




## Setup Instructions
bash
# Clone the repository
git clone https://github.com/your-username/hydroponic-crop-scraper.git
cd hydroponic-crop-scraper

# Install dependencies
pip install -r requirements.txt

# Add API keys in a .env file

# Run the Streamlit app
streamlit run app.py





