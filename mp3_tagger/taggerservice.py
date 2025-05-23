from pathlib import Path

from mutagen.mp3 import EasyMP3


class MP3Tagger:
    """
    This class is used for performing tasks on mp3 files
    """
    def __init__(self):
        self.path = None

    def check_file(self):
        if not self.path.is_file() or not self.path.exists():
            return False
        if self.path.suffix.lower() != '.mp3':
            return False


    def set_path(self, path: Path):
        self.path = path

    def set_tags(self, title: str, artist: str):
        if not self.check_file():
            print("Could not set tags")
        audio = EasyMP3(self.path)
        audio['title'] = title
        audio['artist'] = artist
        audio.save()
        print(f"Successfully tagged: '{title}' by '{artist}'")
