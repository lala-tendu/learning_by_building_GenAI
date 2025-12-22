import streamlit as st
import requests
import base64
import os
from dotenv import load_dotenv
from io import BytesIO
from PIL import Image

load_dotenv()

API_KEY = os.getenv("AZURE_API_KEY")
API_URL = os.getenv("AZURE_API_URI")  # add this in .env

st.title("🚀 AI Image Generator")

prompt = st.text_input("Enter your prompt")

if st.button("Generate"):
    if not prompt.strip():
        st.error("Please enter a prompt.")
    else:
        with st.spinner("Generating image..."):

            headers = {
                "Content-Type": "application/json",
                "Authorization": f"Bearer {API_KEY}"
            }

            data = {
                "prompt": prompt,
                "size": "1024x1024",
                "n": 1,
                "model": "flux.2-pro"   
            }

            response = requests.post(API_URL, headers=headers, json=data)
            res_json = response.json()

            # Extract Base64 image
            b64_img = res_json["data"][0]["b64_json"]

            # Decode Base64 → bytes
            img_bytes = base64.b64decode(b64_img)

            # Convert bytes → PIL Image
            img = Image.open(BytesIO(img_bytes))

            st.image(img)

            # Download button
            st.download_button(
                label="📥 Download Image",
                data=img_bytes,
                file_name="generated_image.png",
                mime="image/png"
            )
