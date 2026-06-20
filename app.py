import streamlit as st
from huggingface_hub import InferenceClient
from dotenv import load_dotenv
import os

load_dotenv()

token = os.getenv("HF_TOKEN")

if not token:
    st.error("HF_TOKEN not found in .env file")
    st.stop()

client = InferenceClient(
    token=token
)

st.title("FLUX VISION")

prompt = st.text_input("Enter your prompt")

if st.button("Generate Image"):

    if prompt:

        with st.spinner("Generating image..."):

            try:

                image = client.text_to_image(
                    prompt=prompt,
                    model="black-forest-labs/FLUX.1-schnell"
                )

                st.image(image)

            except Exception as e:
                st.error(f"Error: {str(e)}")