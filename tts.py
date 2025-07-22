import streamlit as st
import openai
from io import BytesIO
import base64
from dotenv import load_dotenv
import os

# Load environment variables from .env file
load_dotenv()

# Set your OpenAI API key from environment variable
openai.api_key = os.getenv("OPENAI_API_KEY")

st.title("🗣️ OpenAI Text-to-Speech Demo")

# Select inputs
voice = st.selectbox("Choose a voice", ["alloy", "echo", "fable", "onyx", "nova", "shimmer"])
model = st.selectbox("Choose a model", ["tts-1", "tts-1-hd"])
speed = st.selectbox("Choose speech speed", ["0.25", "0.5", "1.0", "1.5", "2.0"])

# Text input
text_input = st.text_area("Enter text to convert to speech", "Hello! This is a demo using OpenAI's TTS.")

if st.button("Generate Speech"):
    try:
        with st.spinner("Generating..."):
            response = openai.audio.speech.create(
                model=model,
                voice=voice,
                input=text_input,
                speed=float(speed)
            )
            audio_bytes = response.read()

            st.audio(audio_bytes, format="audio/mp3")
            b64 = base64.b64encode(audio_bytes).decode()
            href = f'<a href="data:audio/mp3;base64,{b64}" download="output.mp3">⬇️ Download Audio</a>'
            st.markdown(href, unsafe_allow_html=True)

    except Exception as e:
        st.error(f"Error: {str(e)}")
