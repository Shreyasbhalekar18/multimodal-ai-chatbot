import whisper
import pytesseract
from PIL import Image
import fitz  # PyMuPDF

def chat_with_multimodal(file, question):
    if file.type.startswith("image"):
        image = Image.open(file)
        text = pytesseract.image_to_string(image)
    elif file.type.startswith("audio"):
        model = whisper.load_model("base")
        audio_path = "/tmp/audio.wav"
        with open(audio_path, "wb") as f:
            f.write(file.read())
        result = model.transcribe(audio_path)
        text = result["text"]
    elif file.type.endswith("pdf"):
        pdf = fitz.open(stream=file.read(), filetype="pdf")
        text = ""
        for page in pdf:
            text += page.get_text()
    else:
        return "Unsupported file type"

    # Dummy LLM call
    return f"🧠 Based on your file, this is a placeholder response to: '{question}'\n\nExtracted: {text[:300]}"