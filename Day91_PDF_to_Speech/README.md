# Day 91: PDF to Speech Converter – Google Cloud TTS App 

This project transforms a PDF document into spoken audio using **Google Cloud Text-to-Speech**. It extracts text from a PDF, splits it into manageable chunks, and generates high-quality `.mp3` files for each segment — perfect for listening to books, articles, or notes.

---

## Features

* Converts full **PDF documents** to speech
* Automatically **extracts and splits text** into chunks under 5000 bytes
* Generates **MP3 files** using Google Cloud TTS
* Skips chunks that exceed API size limits with warnings
* Clean **console logs** showing progress and chunk sizes
* Neutral **English voice** with natural cadence
* Suppresses PyPDF2 warnings for cleaner output

---

## Technologies Used

* **Python**
* **Google Cloud Text-to-Speech API** – for generating high-quality audio
* **PyPDF2** – for PDF text extraction
* **re** – to split text into sentence-level chunks
* **os**, **logging** – for environment setup and log handling

---

## How to Run

1. **Clone the repository or copy the code**:

   ```bash
   git clone https://github.com/thupham96/100-python-projects.git
   cd Day91_PDF_to_Speech
   ```

2. **Set up Google Cloud credentials**:

   * Create a project at [console.cloud.google.com](https://console.cloud.google.com/)
   * Enable the **Text-to-Speech API**
   * Download your **service account JSON key**
   * Set the environment variable:

   ```bash
   export GOOGLE_APPLICATION_CREDENTIALS="your-key.json"
   ```

3. **Install dependencies**:

   ```bash
   pip install google-cloud-texttospeech PyPDF2
   ```

4. **Place your target PDF** (e.g., `The Little Prince.pdf`) in the same directory.

5. **Run the script**:

   ```bash
   python main.py
   ```

---

## Example Usage

1. The script extracts text from `The Little Prince.pdf`.

2. Text is split into byte-safe chunks using sentence boundaries.

3. Each chunk is passed to the Google TTS API.

4. Resulting audio files are saved as:

   ```
   output_part_1.mp3
   output_part_2.mp3
   ...
   ```

5. Console logs display:

   ```
   Chunk 1 = 3174 bytes
   Saved output_part_1.mp3
   Chunk 2 = 4410 bytes
   Saved output_part_2.mp3
   ```

---

## What I Learned

* How to **parse and clean PDF text** using PyPDF2 and regular expressions
* Working within **byte limits** for Google Cloud TTS input
* Managing **chunked audio generation** to avoid API size errors
* Using **service account credentials** and environment variables with Google Cloud
* Automating document-to-audio conversion workflows in Python
