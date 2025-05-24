from pathlib import Path

class FileService:
    def __init__(self):
        self.path = None

    def set_path(self, path):
        self.path = Path(path)

    def read_folder_mp3_content(self):
        mp3_files = []
        for file in self.path.iterdir():
            if file.is_file() and file.suffix.lower() == '.mp3':
                mp3_files.append(file)
        return mp3_files

if __name__ == '__main__':
    f_service = FileService()
    f_service.set_path('E:/Music/List')
    print(f_service.read_folder_mp3_content())