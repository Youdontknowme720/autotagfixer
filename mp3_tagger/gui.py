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

        self.tag_frame = ttk.Frame(root)
        self.tag_frame.pack(pady=10)

    def select_file(self):
        path = filedialog.askopenfilename(filetypes=[('MP3 Files', '*.mp3')])
        if path:
            self.file_path.set(path)
            self.update_tags_ui()

    def update_tags_ui(self):
        for widget in self.tag_frame.winfo_children():
            widget.destroy()

        for label, var in self.tags.items():
            ttk.Label(self.tag_frame, text=label).pack(anchor='w')
            ttk.Entry(self.tag_frame, textvariable=var, width=50).pack(pady=(0, 5))


        ttk.Button(self.tag_frame, text="Set Tags", command=self.set_mp3_tags, bootstyle=SUCCESS).pack(pady=10)

        self.status_label = ttk.Label(self.tag_frame, text="", bootstyle=INFO)
        self.status_label.pack()


    def set_mp3_tags(self):
        mp3_tagger.set_path(Path(self.file_path.get()))
        print(mp3_tagger.path)
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