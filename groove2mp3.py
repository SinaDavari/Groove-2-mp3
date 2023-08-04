# -*- coding: utf-8 -*-
"""
This is a very simple script to copy the musics in a Groove Music ZPL playlist
into a new folder to be uploaded to a drive or be shared.
Cheers! 

author: Sina Davari
8/4/2023
"""

import os
import shutil
from bs4 import BeautifulSoup

def copy_files(file_path, target_folder):
    with open(file_path, 'r', encoding='utf-8') as f:
        contents = f.read()

    soup = BeautifulSoup(contents, 'lxml')

    media_files = soup.findAll('media')

    if not os.path.exists(target_folder):
        os.makedirs(target_folder)

    for media in media_files:
        src = media.get('src')
        filename = os.path.basename(src)
        target = os.path.join(target_folder, filename)
        try:
            if not os.path.exists(target):
                shutil.copy2(src, target)
                print(f"Copied {src} to {target}")
            else:
                print(f"File {src} already exists in the target folder. Skipping...")
        except FileNotFoundError:
            print(f"File {src} not found. Moving to the next file...")

copy_files('F:/muzic/Miracle.zpl', 'F:/MMM')
