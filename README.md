# Product-Extraction
# Smart Crop Scraper

A smart AI-powered web tool that extracts structured product data (crop name and price per unit) from e-commerce websites. Built using **Firecrawl** for web scraping and **Mistral via OpenRouter**, all wrapped inside a user-friendly **Streamlit** app.

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
```
## 📸 Screenshots

### Screenshot 1 
![Screenshot 1](https://github.com/user-attachments/assets/0f26c09a-f498-4fd0-9467-dc9c183f0619)

### Screenshot 2 
![Screenshot 2](https://github.com/user-attachments/assets/5bad1093-eeb8-41a3-bd8a-7ab2338f2590)

### Screenshot 3
![Screenshot 3](https://github.com/user-attachments/assets/12a45f60-c1cc-4eea-84ef-cc8952fbbfbd)

## 🛠️ Setup Instructions

```bash
# Clone the repository
git clone https://github.com/your-username/hydroponic-crop-scraper.git
cd hydroponic-crop-scraper

# Install dependencies
pip install -r requirements.txt

# Set up environment variables (create a .env file)
echo "FIRECRAWL_API_KEY=your_key_here" > .env
echo "OPENROUTER_API_KEY=your_key_here" >> .env

# Run the app
streamlit run app.py






