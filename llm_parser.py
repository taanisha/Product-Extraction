import requests
import os
from dotenv import load_dotenv

load_dotenv()
OPENROUTER_API_KEY=os.getenv("OPENROUTER_API_KEY")

def extract_product_data(markdown_text):
    url = "https://openrouter.ai/api/v1/chat/completions"  # or OpenRouter's endpoint
    headers = {
        "Authorization": f"Bearer {OPENROUTER_API_KEY}",
        "Content-Type": "application/json"
    }

    messages = [
    {
        "role": "system",
        "content": "You are an intelligent assistant that extracts product information from markdown text. Extract only meaningful product entries."
    },
    {
        "role": "user",
                "content": f"""
Extract ALL product names and their prices from the following Blue Lettuce website markdown. Return ONLY a JSON array in this exact format:

[
  {{ "product": "exact product name", "price": price_number }},
  ...
]

Rules:
- Only extract products that appear after markdown headings (###) and have prices
- Price is always in format '₹XXX.XX'
- If there is a range like ₹XX.XX-₹YY.YY then price is ₹XX.XX calculated by converting the range to numbers(remove ₹ and .00 if present)
- Convert prices to numbers (remove ₹ and .00 if present)
- Ignore any text like 'Add to cart', 'Shop now', 'Quick view'
- Only include real products from this specific content:

{markdown_text}
"""
    }
    ]

    payload = {
        "model": "mistralai/mistral-7b-instruct",  # you can change this to another model if needed
        "messages": messages,
        "temperature": 0.2
    }

    response = requests.post(url, headers=headers, json=payload)
    if response.status_code == 200:
        return response.json()["choices"][0]["message"]["content"]
    else:
        raise Exception(f"LLM error: {response.status_code} - {response.text}")
