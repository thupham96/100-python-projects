from tkinter import *
from tkinter import filedialog, font
from tkinter.ttk import Combobox
from PIL import Image, ImageTk, ImageEnhance, ImageDraw, ImageFont

# Global references
logo_image = None
logo_path = None
original_image = None

# Options
size_options = list(range(8, 73, 2))
spacing_options = list(range(50, 350, 50))
color_options = sorted(['black', 'white', 'red', 'blue', 'green', 'yellow', 'gray'])
text_position_options = {
    "Top": "n",
    "Top-Left": "nw",
    "Top-Right": "ne",
    "Bottom-Left": "sw",
    "Bottom-Right": "se",
    "Center": "center"
}
logo_size_options = [f"{round(x * 0.1, 1)}" for x in range(0, 11)]
opacity_options = [f"{round(x * 0.1, 1)}" for x in range(0, 11)]

# Helper for truetype font
def get_default_font(size):
    try:
        return ImageFont.truetype("arial.ttf", size)
    except:
        return ImageFont.load_default()

# Actions
def open_image():
    global original_image
    file_path = filedialog.askopenfilename(filetypes=[("Image files", "*.png;*.jpg;*.jpeg")])
    if file_path:
        img = Image.open(file_path).convert("RGBA")
        original_image = img.copy()
        canvas.pil_image = img.copy()
        canvas.tk_image = ImageTk.PhotoImage(img)
        canvas.config(width=img.width, height=img.height)
        canvas.delete("all")
        canvas.create_image(0, 0, anchor=NW, image=canvas.tk_image)

def open_text_property_window():
    if not hasattr(canvas, 'pil_image'):
        return

    win = Toplevel(window)
    win.title("Text Properties")
    win.config(padx=20, pady=20, bg='white')

    Label(win, text="Text", bg='white').grid(row=0, column=0)
    text_input = Entry(win)
    text_input.grid(row=0, column=1, pady=10)

    Label(win, text="Color", bg='white').grid(row=1, column=0)
    color_var = StringVar()
    color_cb = Combobox(win, textvariable=color_var, values=color_options, state="readonly")
    color_cb.grid(row=1, column=1, pady=10)
    color_cb.set("black")

    Label(win, text="Size", bg='white').grid(row=2, column=0)
    size_var = StringVar()
    size_cb = Combobox(win, textvariable=size_var, values=size_options, state="readonly")
    size_cb.grid(row=2, column=1, pady=10)
    size_cb.set("30")

    Label(win, text="Tile", bg='white').grid(row=3, column=0)
    tile_var = StringVar()
    tile_cb = Combobox(win, textvariable=tile_var, values=["True", "False"], state="readonly")
    tile_cb.grid(row=3, column=1, pady=10)
    tile_cb.set("False")

    Label(win, text="Spacing", bg='white').grid(row=4, column=0)
    spacing_var = StringVar()
    spacing_cb = Combobox(win, textvariable=spacing_var, values=spacing_options, state="disabled")
    spacing_cb.grid(row=4, column=1, pady=10)
    spacing_cb.set("200")

    def toggle_spacing(*args):
        spacing_cb.config(state="readonly" if tile_var.get() == "True" else "disabled")
    tile_var.trace_add("write", toggle_spacing)

    Label(win, text="Position", bg='white').grid(row=5, column=0)
    pos_var = StringVar()
    pos_cb = Combobox(win, textvariable=pos_var, values=list(text_position_options.keys()), state="readonly")
    pos_cb.grid(row=5, column=1, pady=10)
    pos_cb.set("Center")

    def apply():
        add_text(
            text=text_input.get(),
            color=color_var.get(),
            size=int(size_var.get()),
            tile=tile_var.get(),
            spacing=int(spacing_var.get()),
            position=text_position_options[pos_var.get()]
        )

    Button(win, text="Apply", command=apply).grid(row=6, columnspan=2, pady=10)

def open_logo_property_window():
    global logo_image, logo_path
    if not hasattr(canvas, 'pil_image'):
        return

    if not logo_image:
        logo_path = filedialog.askopenfilename(filetypes=[("Image files", "*.png;*.jpg;*.jpeg")])
        if not logo_path:
            return
        logo_image = Image.open(logo_path).convert("RGBA")

    win = Toplevel(window)
    win.title("Logo Properties")
    win.config(padx=20, pady=20, bg='white')

    Label(win, text="Size", bg='white').grid(row=0, column=0)
    size_var = StringVar()
    size_cb = Combobox(win, textvariable=size_var, values=logo_size_options, state="readonly")
    size_cb.grid(row=0, column=1, pady=10)
    size_cb.set("0.1")

    Label(win, text="Tile", bg='white').grid(row=1, column=0)
    tile_var = StringVar()
    tile_cb = Combobox(win, textvariable=tile_var, values=["True", "False"], state="readonly")
    tile_cb.grid(row=1, column=1, pady=10)
    tile_cb.set("False")

    Label(win, text="Spacing", bg='white').grid(row=2, column=0)
    spacing_var = StringVar()
    spacing_cb = Combobox(win, textvariable=spacing_var, values=spacing_options, state="disabled")
    spacing_cb.grid(row=2, column=1, pady=10)
    spacing_cb.set("200")

    def toggle_spacing(*args):
        spacing_cb.config(state="readonly" if tile_var.get() == "True" else "disabled")
    tile_var.trace_add("write", toggle_spacing)

    Label(win, text="Opacity", bg='white').grid(row=3, column=0)
    opacity_var = StringVar()
    opacity_cb = Combobox(win, textvariable=opacity_var, values=opacity_options, state="readonly")
    opacity_cb.grid(row=3, column=1, pady=10)
    opacity_cb.set("1")

    def apply():
        add_logo(float(size_var.get()), tile_var.get(), int(spacing_var.get()), float(opacity_var.get()))

    Button(win, text="Apply", command=apply).grid(row=4, columnspan=2, pady=10)

def add_text(text, color, size, tile, spacing, position):
    if not hasattr(canvas, 'pil_image'):
        return

    img = canvas.pil_image.copy()
    draw = ImageDraw.Draw(img)
    font_obj = get_default_font(size)
    w, h = img.size

    if tile == "True":
        for y in range(0, h, spacing):
            for x in range(0, w, spacing):
                draw.text((x, y), text, fill=color, font=font_obj)
    else:
        bbox = draw.textbbox((0, 0), text, font=font_obj)
        text_width = bbox[2] - bbox[0]
        text_height = bbox[3] - bbox[1]

        anchor_pos = {
            "center": ((w - text_width) / 2, (h - text_height) / 2),
            "n": ((w - text_width) / 2, 10),
            "ne": (w - text_width - 10, 10),
            "e": (w - text_width - 10, (h - text_height) / 2),
            "se": (w - text_width - 10, h - text_height - 10),
            "s": ((w - text_width) / 2, h - text_height - 10),
            "sw": (10, h - text_height - 10),
            "w": (10, (h - text_height) / 2),
            "nw": (10, 10)
        }

        x, y = anchor_pos.get(position, ((w - text_width) / 2, (h - text_height) / 2))
        draw.text((x, y), text, fill=color, font=font_obj)

    canvas.pil_image = img
    canvas.tk_image = ImageTk.PhotoImage(img)
    canvas.delete("all")
    canvas.create_image(0, 0, anchor=NW, image=canvas.tk_image)

def add_logo(size, tile, spacing, opacity):
    global logo_image
    if original_image is None or logo_image is None:
        return

    logo = logo_image.resize((int(logo_image.width * size), int(logo_image.height * size)), Image.LANCZOS)
    alpha = logo.split()[3].point(lambda p: int(p * opacity))
    logo.putalpha(alpha)

    img = canvas.pil_image.copy()
    iw, ih = img.size
    lw, lh = logo.size

    if tile == "True":
        for y in range(0, ih, spacing):
            for x in range(0, iw, spacing):
                img.paste(logo, (x, y), logo)
    else:
        position = ((iw - lw) // 2, (ih - lh) // 2)
        img.paste(logo, position, logo)

    canvas.pil_image = img
    canvas.tk_image = ImageTk.PhotoImage(img)
    canvas.delete("all")
    canvas.create_image(0, 0, anchor=NW, image=canvas.tk_image)

def save_image():
    if hasattr(canvas, 'pil_image') and canvas.pil_image:
        file_path = filedialog.asksaveasfilename(defaultextension=".png")
        if file_path:
            canvas.pil_image.save(file_path)

def reset():
    global logo_image, logo_path, original_image
    logo_image = None
    logo_path = None
    original_image = None
    canvas.delete("all")
    canvas.config(width=200, height=224)

# GUI
window = Tk()
window.title("Image Watermarking Tool")
window.config(padx=20, pady=20, bg='white')
font_options = sorted(font.families())

Button(window, text="Upload Image", command=open_image).grid(column=0, row=0, pady=10)
Button(window, text="Add Text", command=open_text_property_window).grid(column=1, row=0, pady=10)
Button(window, text="Add Logo", command=open_logo_property_window).grid(column=2, row=0, pady=10)
Button(window, text="Save Image", command=save_image).grid(column=3, row=0, pady=10)
Button(window, text="Reset", command=reset).grid(column=4, row=0, pady=10)

canvas = Canvas(width=200, height=224, highlightthickness=0, bg='white')
canvas.grid(column=0, row=1, columnspan=5, pady=10)

window.mainloop()
