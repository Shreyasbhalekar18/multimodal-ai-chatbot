# 🤖 Multimodal Chatbot System

> A smart AI-powered chatbot that supports PDF, image, and audio inputs using GenAI, Whisper, CLIP, and other state-of-the-art models.

## 🧠 Overview

This project is a **Multimodal Chatbot System** designed to understand and respond to **text**, **PDFs**, **images**, and **audio**. It combines the capabilities of various advanced AI models like:

- **LLMs (e.g., GPT-4)** for natural language conversations.
- **Whisper** for speech-to-text.
- **CLIP** for image understanding.
- **LangChain** and **FAISS** for document-based memory and semantic search.

---

## 📦 Features

✅ Accepts text, image (JPG/PNG), PDF, and audio (MP3/WAV)  
✅ Transcribes audio using Whisper  
✅ Extracts text & answers from PDFs  
✅ Understands visual content using CLIP  
✅ Stores and retrieves user interactions using Vector DB  
✅ Streamlit or Gradio frontend interface  
✅ Modular backend with FastAPI / Flask

---

## 🗂️ Project Structure

multimodal-chatbot/
│
├── backend/
│ ├── app.py # FastAPI or Flask server
│ ├── handlers/
│ │ ├── text_handler.py
│ │ ├── pdf_handler.py
│ │ ├── image_handler.py
│ │ ├── audio_handler.py
│ │ └── vector_store.py
│ └── models/
│ ├── llm_interface.py
│ ├── whisper_model.py
│ └── clip_model.py
│
├── frontend/
│ ├── app.py # Streamlit or Gradio frontend
│ └── components/
│ ├── chat_ui.py
│ └── uploader.py
│
├── data/
│ └── uploaded_files/ # Stores uploaded PDFs/images/audio
│
├── requirements.txt
└── README.md

yaml
Copy
Edit

---

## 🚀 Getting Started

### 🔧 Prerequisites

- Python 3.9+
- Virtual environment (`venv` or `conda`)
- GPU (optional, for Whisper and CLIP)

### 📥 Installation

```bash
git clone https://github.com/your-username/multimodal-chatbot.git
cd multimodal-chatbot

# Create virtual environment
python -m venv venv
source venv/bin/activate  # or venv\Scripts\activate on Windows

# Install dependencies
pip install -r requirements.txt
🛠️ Run the App
🖥️ Backend (FastAPI)
bash
Copy
Edit
cd backend
uvicorn app:app --reload
🧑‍💻 Frontend (Streamlit or Gradio)
bash
Copy
Edit
cd frontend
streamlit run app.py
# OR
python app.py  # If using Gradio
🔍 How It Works
Input Type	Processing Model	Output
Text	GPT-4 / OpenAI API	Chat response
PDF	LangChain + FAISS	Answers to questions from documents
Image	OpenAI CLIP	Description, captioning, and context
Audio	Whisper (open-source or OpenAI API)	Transcribed text

🧠 Models Used
OpenAI GPT-4 / GPT-3.5 – Text generation

Whisper – Speech recognition

CLIP – Vision-language understanding

LangChain + FAISS – PDF semantic QA

✨ Future Scope
🔐 Add user authentication

🌍 Multilingual support

🧠 Connect to long-term vector memory (e.g., Pinecone)

💬 Context-aware history

📱 Deploy to Hugging Face Spaces or Streamlit Cloud

🤝 Contributors
Shreyas Bhalekar – AI & Full Stack Developer

📝 License
MIT License. See LICENSE file for more info.

📸 Screenshots
Chat UI	Image Upload	Audio Transcription
✅	🖼️	🎙️

🙋 FAQ
Q: Can I use this for commercial projects?
Yes, but make sure to follow the licenses of the third-party models (OpenAI, Whisper, etc.).

Q: Does it support real-time voice chat?
No, but you can build that using Whisper + TTS like Coqui.ai.

🔐 Built with care to bridge the gap between humans and machines, one modality at a time.

