#  FLUX Vision - AI Image Generator

An AI-powered text-to-image generation application built with **Python**, **Streamlit**, and **Hugging Face FLUX.1-Schnell**. The application converts natural language prompts into high-quality AI-generated images in real time.

---

#  Project Overview

FLUX Vision is a Generative AI application that allows users to create images simply by entering a text prompt. The application uses the **FLUX.1-Schnell** model from Black Forest Labs through the Hugging Face Inference API to generate realistic and creative images.

The project demonstrates how modern diffusion models can be integrated into web applications using Streamlit and Hugging Face APIs.

---

#  Features

- AI-powered text-to-image generation
- Simple and interactive Streamlit interface
- High-quality image generation using FLUX.1-Schnell
- Real-time image creation
- Secure API key management with `.env`
- Fast inference using Hugging Face Inference API

---

# Technologies Used

- Python
- Streamlit
- Hugging Face Hub
- FLUX.1-Schnell
- Generative AI
- Deep Learning
- python-dotenv

---

#  How the System Works

The application follows these steps:

1. User enters a text prompt.
2. The prompt is sent to the Hugging Face Inference API.
3. The FLUX.1-Schnell model generates an image.
4. The generated image is returned to the application.
5. Streamlit displays the image instantly.

---

#  Project Structure

```
project/
│
├── app.py
├── .env
├── requirements.txt
└── README.md
```

---

#  Installation

## Clone the repository

```bash
git clone https://github.com/your-username/your-repository.git
cd your-repository
```

## Create a virtual environment (Optional)

```bash
python -m venv venv
```

## Activate the virtual environment

### Windows

```bash
venv\Scripts\activate
```

### Linux/macOS

```bash
source venv/bin/activate
```

---

## Install Dependencies

```bash
pip install -r requirements.txt
```

or install manually

```bash
pip install streamlit huggingface_hub python-dotenv
```

---

#  Environment Variables

Create a `.env` file in the project directory.

```env
HF_TOKEN=your_huggingface_api_token
```

---

#  Running the Project

Run the Streamlit application:

```bash
streamlit run app.py
```

The application will open automatically in your web browser.

---

#  AI Model

**Model Used**

- **FLUX.1-Schnell**
- Provider: Black Forest Labs
- Hosted on Hugging Face Inference API

The model generates high-quality images from natural language prompts using advanced generative AI techniques.

---

# Code Workflow

## Load Environment Variables

```python
load_dotenv()
token = os.getenv("HF_TOKEN")
```

## Create Hugging Face Client

```python
client = InferenceClient(
    token=token
)
```

## Generate Image

```python
image = client.text_to_image(
    prompt=prompt,
    model="black-forest-labs/FLUX.1-schnell"
)
```

## Display Image

```python
st.image(image)
```

---

#  Example

### Input Prompt

```
A futuristic city at sunset with flying cars and neon lights.
```

### Output

- AI-generated image based on the prompt
- Displayed instantly within the Streamlit application

---

# Applications

- AI Art Generation
- Graphic Design
- Digital Content Creation
- Marketing and Advertising
- Concept Art
- Story Illustration
- Social Media Content
- Educational Demonstrations

---

#  Future Improvements

- Download generated images
- Image history
- Multiple image generation
- Image style selection
- Prompt enhancement
- Negative prompt support
- High-resolution image generation
- Image editing and variations

---

#  Learning Outcomes

This project demonstrates:

- Generative AI concepts
- Text-to-image generation
- Hugging Face Inference API integration
- Streamlit web application development
- Environment variable management
- API-based AI model deployment

---

#  License

This project is licensed under the MIT License.

---

#  0100011101101111011010110111010101101100

Developed using Python, Streamlit, and Hugging Face FLUX.1-Schnell to demonstrate AI-powered text-to-image generation with a simple and interactive web interface.
