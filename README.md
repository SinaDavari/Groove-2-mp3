# Groove-2-mp3
## Microsoft Groove Playlist Exporter
This is a Python script designed to help you copy your music from a Microsoft Groove playlist to a set of MP3 files. It can come in handy when you want to upload your music to a drive, or share it with your friends.

### Problem Statement
For users who have been using the Microsoft Groove app for their music needs, sharing playlists across different accounts can be a challenge. While the MP3s you own can be stored on OneDrive and played across different Outlook accounts, the playlist data doesn't seem to follow the same path.

This script is built to address this specific issue: sharing the songs in your Groove playlists with others, or transferring them between your own accounts.

### How It Works
This script reads a Groove playlist file (in HTML format), finds all the tracks, and copies them to a designated folder. You can then upload this folder to OneDrive or any other cloud storage service, and share it with another account.

### How to Use
First, find your Groove playlist .zpl file.
Call the function copy_files with the file path of the .zpl file and the target folder/directory where you want to store the MP3s.
The script will create the target directory if it doesn't exist, then it will copy the MP3 files from the playlist into that directory.
If a file is already present in the target directory, the script will skip it and move to the next one. It will also handle cases where the source file is not found.
Notes

This README gives a brief description of the project, the problem it solves, how it works, and how to use it. It also notes a current limitation (the lack of playlist metadata handling). Feel free to edit this template to better suit your needs.
