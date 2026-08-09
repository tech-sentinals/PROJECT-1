import os
from pathlib import Path
from flask import Flask, request, jsonify
from PyPDF2 import PdfReader
from google.cloud import texttospeech

app = Flask(__name__)
UPLOAD_DIR = Path("uploads")
OUTPUT_DIR = Path("output")
UPLOAD_DIR.mkdir(exist_ok=True)
OUTPUT_DIR.mkdir(exist_ok=True)


def extract_text(path: Path) -> str:
    reader = PdfReader(str(path))
    return "\n".join(page.extract_text() or "" for page in reader.pages).strip()


def synthesize(text: str, output: Path) -> None:
    client = texttospeech.TextToSpeechClient()
    response = client.synthesize_speech(
        input=texttospeech.SynthesisInput(text=text[:4500]),
        voice=texttospeech.VoiceSelectionParams(language_code="en-US", ssml_gender=texttospeech.SsmlVoiceGender.NEUTRAL),
        audio_config=texttospeech.AudioConfig(audio_encoding=texttospeech.AudioEncoding.MP3),
    )
    output.write_bytes(response.audio_content)

@app.post("/api/convert")
def convert():
    uploaded = request.files.get("pdf")
    if not uploaded or not uploaded.filename.lower().endswith(".pdf"):
        return jsonify(error="Upload a PDF file."), 400
    safe_name = Path(uploaded.filename).name
    pdf_path = UPLOAD_DIR / safe_name
    audio_path = OUTPUT_DIR / f"{pdf_path.stem}.mp3"
    uploaded.save(pdf_path)
    text = extract_text(pdf_path)
    if not text:
        return jsonify(error="No extractable text found in the PDF."), 422
    synthesize(text, audio_path)
    return jsonify(message="Conversion complete", audio=str(audio_path), characters=len(text))

@app.get("/health")
def health():
    return jsonify(status="ok")

if __name__ == "__main__":
    app.run(debug=True)
