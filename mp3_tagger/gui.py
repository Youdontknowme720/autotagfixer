import tkinter as tk
from pathlib import Path
from tkinter import filedialog
import ttkbootstrap as ttk
from mutagen.mp3 import EasyMP3
from ttkbootstrap.constants import *

class AutoUI:
    def __init__(self, root):
        self.root = root
        self.root.title('Automated MP3 Tagger')

        self.file_path = ttk.StringVar()
        self.success = ttk.StringVar()

        ttk.Label(root, text="Chose your MP3 File").pack(pady=5)
        ttk.Entry(root, textvariable=self.file_path, width=50).pack(padx=10)
        ttk.Button(root, text="Search", command=self.select_file).pack(pady=5)

        self.tags = {
            "Title": ttk.StringVar(),
            "Artist": ttk.StringVar()
        }

        for label, var in self.tags.items():
            ttk.Label(root, text=label).pack(pady=2)
            ttk.Entry(root, textvariable=var, width=50).pack()

        ttk.Button(root, text="Set Tags", command=self.set_tags, style=OUTLINE).pack(pady=5)
        self.status_label = ttk.Label(root, text="")
        self.status_label.pack(pady=5)

    def select_file(self):
        path = filedialog.askopenfilename(filetypes=[('MP3 Files', '*.mp3')])
        if path:
            self.file_path.set(path)

    def set_tags(self):
        path = Path(self.file_path.get())
        title = self.tags['Title'].get()
        artist = self.tags['Artist'].get()
        try:
            audio = EasyMP3(path)
            audio['title'] = title
            audio['artist'] = artist
            audio.save()
            self.status_label.config(text=f"Successfully wrote tags \nTitle: {title}\nArtist: {artist}\n to File: {path.name}")
        except Exception as e:
            print(e)

if __name__ == '__main__':
    app = ttk.Window(themename="darkly", size=(800,600))
    AutoUI(app)
    app.mainloop()