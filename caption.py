import requests
import streamlit as st

API_URL = "https://api-inference.huggingface.co/models/Salesforce/blip-image-captioning-large"
headers = {"Authorization": "Bearer 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"}

def query(filename):
    with open(filename, "rb") as f:
        data = f.read()
    response = requests.post(API_URL, headers=headers, data=data)
    return response.json()

#output = query("/content/download.jpg")

st.file_uploader("Upload an image",type="jpg")