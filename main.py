import streamlit as st

st.title("AI webscraper")
url =st.text_input("Enter a URL: ")

if st.button("Scrape site"):
    st.write("Scrapind the website")