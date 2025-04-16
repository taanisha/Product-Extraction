import streamlit as st
from firecrawl_scraper import scrape_with_firecrawl
from llm_parser import extract_product_data
import json  # Don't forget to import json

st.set_page_config(page_title="Crop Price Extractor", layout="centered")
st.title("Smart Crop Extractor")

url = st.text_input("Enter the url:", value="https://www.bluelettuce.in/our-products/")

if st.button("Extract Product Data"):
    with st.spinner("Scraping and Parsing"):
        try:
            firecrawl_response = scrape_with_firecrawl(url)
            
            # First parse the response if it's a string
            if isinstance(firecrawl_response, str):
                try:
                    response_data = json.loads(firecrawl_response)
                except json.JSONDecodeError as e:
                    st.error(f"Failed to parse JSON response: {str(e)}")
                    exit
            
            # Get the markdown text
            markdown_text = response_data.get("data", {}).get("markdown", "")
            
            if not markdown_text:
                st.error("No markdown content found in the scraped data")
                exit
                
            # Extract product data from markdown
            structured_output = extract_product_data(markdown_text)

            print("Successful!")
            st.markdown("Extracted Data")
            
            # Try to parse the output to verify it's valid JSON
            try:
                parsed_output = json.loads(structured_output)
                st.json(parsed_output)
            except json.JSONDecodeError:
                st.error("LLM returned invalid JSON format")
                st.text(structured_output)
                
        except Exception as e:
            st.error(f"Error: {str(e)}")