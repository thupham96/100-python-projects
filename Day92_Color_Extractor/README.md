# Day 92: Color Extractor – Python Tkinter + Pillow App

This project is a **desktop application** that lets you open any image and instantly discover its **top 10 dominant colors**.
It provides a live preview of the image, displays the color swatches with HEX/RGB values and usage percentages, and allows easy copying of the HEX list to the clipboard.

---

## Features

* **Open an image** of nearly any format (PNG, JPG, JPEG, WebP, BMP, GIF, TIFF)
* **Preview the image** in the app window with automatic downscaling for speed
* Extracts and displays the **top 10 colors** with:

  * **HEX code**
  * **RGB tuple**
  * **Percentage of image coverage**
* **Copy HEX list** to clipboard with one click
* Handles transparent pixels gracefully by compositing on white
* Responsive **Tkinter GUI** with clear color swatches

---

## Technologies Used

* **Python**
* **Tkinter** – for the graphical user interface
* **Pillow (PIL)** – for image loading, resizing, quantization, and color analysis
* **collections.Counter** – for counting color occurrences

---

## How to Run

1. **Clone the repository or copy the code**:

   ```bash
   git clone https://github.com/thupham96/100-python-projects.git
   cd Day92_Color_Extractor
   ```

2. **Install dependencies** (use a virtual environment if preferred):

   ```bash
   pip install pillow
   ```

3. **Run the app**:

   ```bash
   python app.py
   ```

4. **Use the interface**:

   * Click **“Open Image…”** to choose a file.
   * View the **image preview** and the **top 10 colors** with HEX/RGB/percentage.
   * Click **“Copy HEX List”** to copy all HEX codes to your clipboard.

---

## Example Output (GUI)

*Left side:* Image preview
*Right side:*

```
1. #AABBCC  RGB(170, 187, 204)  18.5%
2. #334455  RGB(51, 68, 85)     14.2%
...
10. #F1E2D3 RGB(241, 226, 211)   2.3%
```

Each color row shows a **swatch**, HEX code, RGB values, and percentage of coverage.

---

## What I Learned

* Building a **desktop GUI** with Tkinter frames, buttons, and canvas elements
* Using **Pillow** to resize images, composite transparent pixels, and perform adaptive palette quantization
* Counting color frequencies and calculating **percentage coverage**
* Managing **clipboard operations** in a Python application
* Organizing code into a clean **OOP structure** (`ColorApp` class) with clear separation of GUI and logic

This README follows the Day 93 format while reflecting the unique details of your **Day 92 Color Extractor** project.
