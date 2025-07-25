# 📝 Minutes of Meeting M.O.M

This is a Streamlit-based web application that allows users to upload image files containing handwritten or printed meeting notes. The application then extracts and parses the text from these images, presenting the extracted minutes in a clean and readable format.

👉 [**Click here for the live demo**](https://minutes-of-meetingg.streamlit.app/) 

---
## Screenshots
<img width="1920" height="814" alt="Screenshot (380)" src="https://github.com/user-attachments/assets/c8958bfc-bc22-4937-8b0c-8607626b17af" />

<img width="1920" height="836" alt="Screenshot (381)" src="https://github.com/user-attachments/assets/4607ca44-c3d8-49fe-9cae-9bbcd2ca1863" />

<img width="1920" height="681" alt="Screenshot (382)" src="https://github.com/user-attachments/assets/b84e805b-15d2-4117-b146-74fdeba8c5e0" />

## 🚀 Features

- 📁 **File Browser**: Upload image files directly through the interface.
- 🖼️ **Image Upload**: Accepts image formats (e.g., PNG, JPG).
- 🔍 **Text Extraction**: Uses Optical Character Recognition (OCR) to extract text from uploaded images.
- 📋 **Parsed Output**: Displays the structured minutes of the meeting from the extracted content.
- ✅ **Simple Interface**: Built using Streamlit for quick and interactive deployment.

## 🛠️ Technologies Used

- **Python 3**
- **Streamlit** – Web UI framework
- **Pytesseract / EasyOCR** – OCR libraries for extracting text from images
- *(Optional)* **spaCy / regex** – For advanced text parsing

## 📂 How to Use Locally

1. **Clone the Repository**
   ```bash
   git clone https://github.com/yourusername/minutes-of-meeting-streamlit.git
   cd minutes-of-meeting-streamlit
