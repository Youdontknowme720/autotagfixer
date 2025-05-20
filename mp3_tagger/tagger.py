import argparse
import sys
from pathlib import Path

from mutagen.mp3 import EasyMP3

parser = argparse.ArgumentParser(description="Sets automatically MP3-tags")
parser.add_argument(
    "-p",
    type=str,
    required=True,
    help="Path to the MP3-File"
)
parser.add_argument(
    "-a",
    type=str,
    required=True,
    help="This option is used for setting the artist tag"
)
parser.add_argument(
    "-t",
    type=str,
    required=True,
    help="This option is used for setting the title tag"
)

args = parser.parse_args()
path = Path(args.p)
artist = args.a
title = args.t


def main():
    if not path.is_file() or not path.exists():
        print("File does not exists")
        return 1
    if path.suffix.lower() != '.mp3':
        print("Pleas enter a .mp3 file")
        return 1
    if artist is None or title is None:
        print("Please provide both artist (-a) and title (-t).")
        return 1

    audio = EasyMP3(path)

    if audio:
        for key in audio:
            print(f"Already found {key}: \t{audio[key]}")
        tag_change_choice= input("Are you sure you want to change tags?:\t y/n")
        if tag_change_choice.lower() != "y":
            print("No changes performed")
            return 1

    audio['title'] = title
    audio['artist'] = artist
    audio.save()
    print(f"Successfully tagged: '{title}' by '{artist}'")
    return 0


if __name__ == '__main__':
    sys.exit(main())