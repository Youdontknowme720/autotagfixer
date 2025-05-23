from pathlib import Path
from tkinter import filedialog

import ttkbootstrap as ttk
from ttkbootstrap.constants import *
from taggerservice import MP3Tagger


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

        ttk.Button(root, text="Set Tags", command=self.set_mp3_tags, style=OUTLINE).pack(pady=5)
        self.status_label = ttk.Label(root, text="")
        self.status_label.pack(pady=5)

    def select_file(self):
        path = filedialog.askopenfilename(filetypes=[('MP3 Files', '*.mp3')])
        if path:
            self.file_path.set(path)

    def set_mp3_tags(self):
        mp3_tagger.set_path(Path(self.file_path.get()))
        title = self.tags['Title'].get()
        artist = self.tags['Artist'].get()
        try:
            mp3_tagger.set_tags(title, artist)
            self.status_label.config(text=f"Successfully wrote tags \nTitle: {title}\nArtist: {artist}\n to File: {mp3_tagger.path}")
        except Exception as e:
            print(e)

if __name__ == '__main__':
    mp3_tagger = MP3Tagger()
    app = ttk.Window(themename="darkly", size=(800,600))
    AutoUI(app)
    app.mainloop()