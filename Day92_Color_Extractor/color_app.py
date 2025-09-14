import os.path
from tkinter import Frame, Button, Label, filedialog, messagebox, Canvas

from PIL import ImageTk, Image

APP_TITLE = 'Color Extractor'
MAX_PREVIEW = 480
SAMPLE_EDGE = 600
TOP_N = 10

class ColorApp:
    def __init__(self, root):
        self.root = root
        self.root.title(APP_TITLE)
        self.root.minsize(720, 520)

        self.topbar = Frame(root, padx=12, pady=10)
        self.topbar.pack(fill="x")

        self.open_btn = Button(self.topbar, text="Open Image...", command=self.open_image)
        self.open_btn.pack(side='left')

        self.copy_btn = Button(self.topbar, text="Copy HEX List", command=self.copy_hexes, state="disabled")
        self.copy_btn.pack(side="right", padx=10)

        self.file_label = Label(self.topbar, text="No file selected", anchor="w")
        self.file_label.pack(side="left", padx=10)

        self.main = Frame(root, padx=10, pady=10)
        self.main.pack(fill="both", expand=True)

        self.preview_frame = Frame(self.main)
        self.preview_frame.pack(side="left", fill="both", expand=True)

        self.results_frame = Frame(self.main)
        self.results_frame.pack(side="right", fill="y", expand=True)

        self.preview_label = Label(self.preview_frame, text="", bd=1, relief="sunken")
        self.preview_label.pack(fill="both", expand=True, padx=10)

        self.colors_title = Label(self.results_frame, text="Top 10 Colors", font=("Segoe UI", 12, "bold"))
        self.colors_title.pack(pady=(0, 6))

        self.colors_container = Frame(self.results_frame)
        self.colors_container.pack(fill="y")

        self._preview_img_ref = None
        self._last_results = []
        self._last_path = None

    def open_image(self):
        path = filedialog.askopenfilename(
            title="Choose an image",
            filetypes=[
                ("Images", "*.png;*.jpg;*.jpeg;*.webp;*.bmp;*.gif;*.tif;*.tiff"),
                ("All files", "*.*"),
            ]
        )
        if not path:
            return
        try:
            self._last_path = path
            self.file_label.config(text=os.path.basename(path))
            self.show_preview(path)
            self.run_analysis(path)
        except Exception as e:
            messagebox.showerror("Error", f"{e}")

    def copy_hexes(self):
        if not self._last_results:
            return
        hex_list = ",".join(item["hex"] for item in self._last_results)
        self.root.clipboard_clear()
        self.root.clipboard_append(hex_list)
        self.root.update()
        messagebox.showinfo("Copied", f"Copied HEX list to clipboard\n{hex_list}")

    def show_preview(self, path):
        img = Image.open(path).convert("RGBA")
        img.thumbnail((MAX_PREVIEW, MAX_PREVIEW))
        tk_img = ImageTk.PhotoImage(img)
        self._preview_img_ref = tk_img
        self.preview_label.config(image=tk_img)

    def extract_top_colors(self, path):
        img = Image.open(path).convert("RGBA")
        # Downscale for speed
        img.thumbnail((SAMPLE_EDGE, SAMPLE_EDGE))
        # Composite on white, so transparent/semtransparent pixels don’t skew results
        # Drop alpha
        img = Image.alpha_composite(Image.new("RGBA", img.size, (255,255,255,255)), img).convert("RGB")
        # Reduce colors to exactly n with an adaptive palette
        pal = img.convert("P", palette=Image.ADAPTIVE, colors=TOP_N)
        # Convert back to RGB to count actual (r,g,b) values directly
        rgb = pal.convert("RGB")
        # Count occurrences of each color
        total = rgb.size[0] * rgb.size[1]
        counts = rgb.getcolors(maxcolors=total)
        top = sorted(counts, key=lambda x: x[0], reverse=True)[:TOP_N]
        out = []
        for cnt, (r, g, b) in top:
            out.append({
                "rgb": (r, g, b),
                "hex": f"#{r:02X}{g:02X}{b:02X}",
                "percent": round(100 * cnt / total, 2),
                "count": cnt
            })
        return out

    def run_analysis(self, path):
        results = self.extract_top_colors(path)
        self._last_results = results
        self.copy_btn.config(state=("normal" if results else "disabled"))
        self.render_results(results)

    def render_results(self, results):
        for child in self.colors_container.winfo_children():
            child.destroy()

        if not results:
            Label(self.colors_container, text="No colors found").pack()
            return

        for idx, item in enumerate(results, start=1):
            row = Frame(self.colors_container)
            row.pack(fill="x", pady=4)

            sw = Canvas(row, width=28, height=28, highlightthickness=1, highlightbackground="#DDD")
            sw.pack(side='left', padx=(0, 8))
            sw.create_rectangle(0, 0, 28, 28, fill=item["hex"], outline="")

            text = f"{idx}.  {item['hex']}   RGB{item['rgb']}   {item['percent']}%"
            Label(row, text=text, font=("Segoe UI", 10)).pack(side="left")


