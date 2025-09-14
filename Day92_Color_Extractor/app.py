import os
from collections import Counter
from tkinter import Tk, Frame, Button, Label, Canvas, filedialog, messagebox
from PIL import Image, ImageTk
from color_app import ColorApp

MAX_PREVIEW = 480          # Max width/height for preview
ANALYSIS_SAMPLE = 600      # Resize longest edge for analysis speed
PALETTE_SIZE = 64          # Quantization palette size

def main():
    root = Tk()
    app = ColorApp(root)
    root.mainloop()


if __name__ == "__main__":
    main()