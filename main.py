import streamlit as st
from scrape import scrape_website

st.title("AI webscraper")
url =st.text_input("Enter a URL: ")

if st.button("Scrape site"):
    st.write("Scraping the website")
    result = scrape_website(url)
    print(result)