#!/usr/bin/env python3
"""
Rename all images in a folder to "YYYY-MM-DD-HHMMSS-originalname.ext"
based on EXIF DateTimeOriginal. Falls back to file modified time if no EXIF.

Usage:
    python rename_by_exif.py /path/to/folder
"""

import sys
import os
from datetime import datetime
from PIL import Image
from PIL.ExifTags import TAGS

def get_exif_date(path):
    try:
        img = Image.open(path)
        exif = img._getexif()
        if not exif:
            return None
        for tag_id, value in exif.items():
            tag = TAGS.get(tag_id, tag_id)
            if tag == "DateTimeOriginal":
                return datetime.strptime(value, "%Y:%m:%d %H:%M:%S")
    except Exception:
        return None
    return None

def get_fallback_date(path):
    return datetime.fromtimestamp(os.path.getmtime(path))

def main(folder):
    exts = (".jpg", ".jpeg", ".png", ".tiff", ".tif", ".heic")
    files = [f for f in os.listdir(folder) if f.lower().endswith(exts)]

    for fname in files:
        fpath = os.path.join(folder, fname)
        date = get_exif_date(fpath) or get_fallback_date(fpath)
        base = date.strftime("%Y-%m-%d")
        ext = os.path.splitext(fname)[1]

        new_name = f"{base}{ext}"
        new_path = os.path.join(folder, new_name)
        counter = 2
        while os.path.exists(new_path) and new_path != fpath:
            new_name = f"{base}-{counter}{ext}"
            new_path = os.path.join(folder, new_name)
            counter += 1

        os.rename(fpath, new_path)
        print(f"{fname}  ->  {new_name}")

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: python rename_by_exif.py /path/to/folder")
        sys.exit(1)
    main(sys.argv[1])
