from mutagen.mp3 import EasyMP3
import argparse
import os
from pathlib import Path

parser = argparse.ArgumentParser(description="Sets automatically MP3-tags")
parser.add_argument(
    "-p",
    type=str,
    help="Path to the MP3-File"
)
parser.add_argument(
    "-a",
    type=str,
    help="This option is used for setting the artist tag"
)
parser.add_argument(
    "-t",
    type=str,
    help="This option is used for setting the title tag"
)

args = parser.parse_args()
path = Path(args.p)
artist = args.a
title = args.t


def main():
    if not path.is_file() or not path.exists():
        print("File does not exists")
        return 0
    if path.suffix.lower() != '.mp3':
        print("Pleas enter a .mp3 file")
        return 0

    audio = EasyMP3(path)
    audio['title'] = title
    audio['artist'] = artist
    audio.save()


if __name__ == '__main__':
    main()