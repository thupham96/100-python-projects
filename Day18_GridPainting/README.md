# Day 18: Grid Painting

Welcome to the Grid Painting project! This Python program creates a **10x10 dot painting** using the **Turtle graphics** package. The color palette is inspired by **Damien Hirst** and was extracted from one of his paintings using the **colorgram** package. The project primarily focuses on **Turtle graphics** and **GUI interactions**.

---

## How It Works  

### Project Setup:  

- The program uses **Turtle graphics** to create a grid of **colored dots**.  
- A color palette was extracted from a Damien Hirst painting using **colorgram** (`extract_color.py`).  
- The extracted colors were manually selected and stored in a list for use in the painting.  

---

### Program Features:  

1. **Color Extraction**:
   - The `extract_color.py` script extracts colors from an image using the `colorgram` library.
   - Selected colors are copied over into the main painting script for use.

2. **Grid Painting with Turtle**:
   - The script sets up a **10x10 grid** where each dot is a randomly selected color from the palette.
   - Each dot is evenly spaced to create an organized yet vibrant aesthetic.

3. **GUI Interaction**:
   - The painting is displayed on a Turtle graphics screen, allowing users to visually appreciate the result.

---

## How to Run the Program  

1. Clone the repository and navigate to the `Day18_GridPainting` folder:  
   ```bash
   git clone https://github.com/thupham96/100-python-projects.git
   cd 100-python-projects/Day18_GridPainting
   ```

2. Install dependencies:  
   ```bash
   pip install colorgram.py
   ```

3. Run the color extraction script (optional if modifying the palette):  
   ```bash
   python extract_color.py
   ```

4. Run the grid painting script:  
   ```bash
   python grid_painting.py
   ```

---

## Example Run  

When you execute the script, a Turtle graphics window will open and display a **10x10 grid of colored dots**, each dot randomly selected from the predefined color palette.

Example output (text representation):

```plaintext
[●  ●  ●  ●  ●  ●  ●  ●  ●  ●]
[●  ●  ●  ●  ●  ●  ●  ●  ●  ●]
[●  ●  ●  ●  ●  ●  ●  ●  ●  ●]
[●  ●  ●  ●  ●  ●  ●  ●  ●  ●]
[●  ●  ●  ●  ●  ●  ●  ●  ●  ●]
[●  ●  ●  ●  ●  ●  ●  ●  ●  ●]
[●  ●  ●  ●  ●  ●  ●  ●  ●  ●]
[●  ●  ●  ●  ●  ●  ●  ●  ●  ●]
[●  ●  ●  ●  ●  ●  ●  ●  ●  ●]
[●  ●  ●  ●  ●  ●  ●  ●  ●  ●]
```

---

## Technologies Used  

- **Python 3**  
- **Turtle graphics** for GUI painting  
- **Colorgram** for extracting colors from an image  
- **Random module** for color selection  

---

## What I Learned  

- Extracting color palettes from images using **colorgram**.  
- Using **Turtle graphics** to create a structured **grid-based painting**.  
- Managing and manipulating lists of colors for dynamic art creation.  
- Simulating real-world artwork using Python.  

Enjoy using the Grid Painting program and feel free to experiment with different color palettes and grid sizes! 🎨


