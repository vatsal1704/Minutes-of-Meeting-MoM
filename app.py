import os
from dotenv import load_dotenv
load_dotenv()

import streamlit as st 
import google.generativeai as genai
from PIL import Image

# Genai Configuration
genai.configure(api_key=os.getenv("GOOGLE_API_KEY"))
model = genai.GenerativeModel("gemini-2.0-flash")

# Front End
st.header(":blue[Minutes of Meeting] Generator", divider=True)
st.markdown("Minutes of Meeting Generator: Upload your handwritten MOMs")

uploaded_file = st.file_uploader("Upload your Image", type=["jpg", "jpeg", "png"])

if uploaded_file is not None:
    img = Image.open(uploaded_file)
    st.image(img, use_container_width=True)

    prompt = '''
You are an intelligent assistant tasked with generating structured Minutes of Meeting (MoM) based on handwritten notes and to-dos provided as images. Your job is to extract text from the images and organize the information into a clean, professional table with the following columns:
| Particulars (To-Dos) | Deadline | Status (Completed / Pending / Not Started) | % Completion |
Requirements:
OCR: Accurately read and transcribe handwritten text from the uploaded images.
Task Identification: Identify individual to-do items, action points, or tasks from the transcribed text.
Deadline Detection: Detect any mentioned dates or inferred deadlines related to each task. If no deadline is present, leave the field blank or mark as “TBD.”
Status Assignment: Based on context (e.g., checkmarks, strikethroughs, annotations like "done", "in progress", "to-do", etc.), assign a task status:
✅ Completed
🕒 Pending
⏳ Not Started
Completion %: Estimate a percentage completion (e.g., 0%, 50%, 100%) based on the language or markings (e.g., “half done”, “in progress”, “✓✓✓”, etc.).
    '''

    with st.spinner("Extracting and Analysing the Image...."):
        response = model.generate_content([img, prompt])
        st.success("Extraction Completed")
        st.markdown(response.text)
