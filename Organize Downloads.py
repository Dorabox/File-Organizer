# Import the libraries
from os import listdir
from os.path import isfile, join, isdir
import shutil
import magic  

i = 1
# Obtain the path to be organized
file_path = 'D:/Downloads'
 
# Obtain all the items (files and folders) from the path in a list
items = listdir(file_path)

# Lists of file types
media_file_types = ['audio', 'image', 'video']
document_file_types = ['text', 'application/pdf', 'application/msword', 'application/vnd.ms-excel']
compresseddisc_file_types = ['application/zip', 'application/x-7z-compressed', 'application/x-rar-compressed']
executable_file_types = ['application/x-msdownload', 'application/x-sh']
torrent_file_types = ['application/x-bittorrent']

# Destination file paths 
audio_file_path = 'D:/Downloads/Media/Audio'
image_file_path = 'D:/Downloads/Media/Images'
video_file_path = 'D:/Downloads/Media/Videos'
docs_file_path = 'D:/Downloads/Documents/Docs'
pdf_file_path = 'D:/Downloads/Documents/PDFs'
ppt_file_path = 'D:/Downloads/Documents/PPTs'
spreadsheet_file_path = 'D:/Downloads/Documents/Spreadsheets'
text_file_path = 'D:/Downloads/Documents/Text Files'
compressed_file_path = 'D:/Downloads/Compressed Files/Compressed Files'
disc_file_path = 'D:/Downloads/Compressed Files/Disc Files'
executable_file_path = 'D:/Downloads/Executables'
torrent_file_path = 'D:/Downloads/Torrents'
folder_file_path = 'D:/Downloads/Folders'
general_file_path = 'D:/Downloads/General'

# Folder categories
category_folders = ['Media', 'Documents', 'Compressed Files', 'Executables', 'Torrents', 'General']

# Transfer function
def transfer_file(source_path, destination_path):
    shutil.move(source_path, destination_path)
    print(source_path + ' >>> ' + destination_path)

# Loop through the items
for item in items:
    print(i)
    source_path = join(file_path, item)

    # Check if it's a folder
    if isdir(source_path):
        if item in category_folders:
            continue
        else:
            print(f"{item} is a folder.")
            transfer_file(source_path, folder_file_path)

    # If it's a file, use python-magic to detect the file type based on content
    file_type = magic.from_file(source_path, mime=True)  # Detect file type based on content
    print(f"File: {item}, File Type: {file_type}")
    
    if file_type:
        # Media file check
        if 'audio' in file_type:
            transfer_file(source_path, audio_file_path)
        elif 'image' in file_type:
            transfer_file(source_path, image_file_path)
        elif 'video' in file_type:
            transfer_file(source_path, video_file_path)
        # Document file check
        elif 'text' in file_type:
            transfer_file(source_path, text_file_path)
        elif 'pdf' in file_type:
            transfer_file(source_path, pdf_file_path)
        elif 'msword' in file_type or 'word' in file_type:
            transfer_file(source_path, docs_file_path)
        elif 'excel' in file_type:
            transfer_file(source_path, spreadsheet_file_path)
        # Compressed file check
        elif 'zip' in file_type or '7z' in file_type or 'rar' in file_type:
            transfer_file(source_path, compressed_file_path)
        # Executable file check
        elif 'x-msdownload' in file_type or 'sh' in file_type:
            transfer_file(source_path, executable_file_path)
        # Torrent file check
        elif 'bittorrent' in file_type:
            transfer_file(source_path, torrent_file_path)
        else:
            transfer_file(source_path, general_file_path)
    i += 1