                                          FLUX Vision – AI Image Generator

  Overview

FLUX Vision is a simple AI-powered image generation web application built with Streamlit and Hugging Face Inference API.
The application takes a text prompt from the user and generates an image using the FLUX.1-schnell model from Hugging Face.
This project demonstrates how to integrate AI image generation models into a Python web application with a minimal frontend.


  Features
   
> Text-to-image generation using AI
> Simple web interface built with Streamlit
> Uses python-dotenv for secure API token management
> Connects with Hugging Face Hub
> Generates images from natural language prompts
> Real-time loading spinner during image generation
> Error handling for missing API tokens and generation failures


  Tech Stack

> Python 3.x
> Streamlit
> Hugging Face Hub Python Library
> FLUX.1-schnell Model
> python-dotenv


  Project Structure

  
FLUX-Vision
    
    
>app.py              # Main Streamlit application
>.env(API token)      # Environment variables
>requirements.txt   # Project dependencies
>README.md          # Project documentation
