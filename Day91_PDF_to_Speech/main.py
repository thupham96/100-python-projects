from google.cloud import texttospeech
from PyPDF2 import PdfReader
import re
import logging

logging.getLogger("PyPDF2").setLevel(logging.ERROR)

# Set your credentials path
import os
os.environ["GOOGLE_APPLICATION_CREDENTIALS"] = "<YOUR_GOOGLE_APP_CREDENTIALS>.json"

# Initialize client
client = texttospeech.TextToSpeechClient()

# Synthesize text
def synthesize_text(text, index):
    synthesis_input = texttospeech.SynthesisInput(text=text)
    voice = texttospeech.VoiceSelectionParams(
        language_code="en-US",
        ssml_gender=texttospeech.SsmlVoiceGender.NEUTRAL,
    )
    audio_config = texttospeech.AudioConfig(
        audio_encoding=texttospeech.AudioEncoding.MP3,
    )

    response = client.synthesize_speech(
        input=synthesis_input, voice=voice, audio_config=audio_config
    )

    with open(f"output_part_{index}.mp3", "wb") as out:
        out.write(response.audio_content)
        print(f"Saved output_part_{index}.mp3")

# Split text
def split_text_by_bytes(text, byte_limit=4500):
    sentences = re.split(r'(?<=[.!?]) +', text)
    chunks = []
    current = ""

    for sentence in sentences:
        test_chunk = current + sentence + " "
        if len(test_chunk.encode("utf-8")) < byte_limit:
            current = test_chunk
        else:
            if current:
                chunks.append(current.strip())
            current = sentence + " "
    if current:
        chunks.append(current.strip())
    return chunks

# Load pdf text
reader = PdfReader("<YOUR_BOOK>.pdf")
full_text = "\n".join(page.extract_text() for page in reader.pages if page.extract_text())

# Split and synthesize
chunks = split_text_by_bytes(full_text)
for idx, chunk in enumerate(chunks):
    size = len(chunk.encode("utf-8"))
    print(f"Chunk {idx + 1} = {size} bytes")

    if size < 5000:
        synthesize_text(chunk, idx + 1)
    else:
        print(f"⚠️ Skipping chunk {idx + 1} — exceeds 5000 bytes ({size} bytes)")
