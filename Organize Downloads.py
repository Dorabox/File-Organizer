# Python program to automatically organize
# Downloads folder in Python

# Import the libraries
from os import listdir
from os.path import isfile, join
import os
import shutil
i = 1
# Obtain the path to be organized
file_path = 'D:\Downloads'
 
# Obtain all the files from the path in list
files = [f for f in listdir(file_path) if isfile(join(file_path, f))]
 
# Lists of file extensions
media_file_types = ['aif','cda','mid','midi','mp3','mpa','ogg','wav','wma','wpl','ai','bmp','gif','ico','jpeg','jpg','png','ps','psd','scr','svg','tif','tiff','webp','avi','flv','m4v','mkv','mov','mp4','mpg','mpeg','webm','wmv']
document_file_types = ['doc','docx','odt','pdf','rtf','tex','txt','ods','xls','xlsm','csv','xlsx','key','odp','pps','ppt','pptx']
compresseddisc_file_types = ['7z','arj','deb','pkg','rar','rpm','z','zip','bin','dmg','iso','toast','vcd']
executable_file_types = ['bat','exe','com','msi','sh','wsf','gadget']
image_file_types = ['ai','bmp','gif','ico','jpeg','jpg','png','ps','psd','scr','svg','tif','tiff','webp']
video_file_types = ['avi','flv','m4v','mkv','mov','mp4','mpg','mpeg','webm','wmv']
audio_file_types = ['aif','cda','mid','midi','mp3','mpa','ogg','wav','wma','wpl']
docs_file_types = ['doc','docx','odt']
pdf_file_types = ['pdf']
ppt_file_types = ['key','odp','pps','ppt','pptx']
spreadsheet_file_types = ['ods','xls','xlsm','csv','xlsx']
text_file_types = ['rtf','tex','txt']
compressed_file_types = ['7z','arj','deb','pkg','rar','rpm','z','zip',]
disc_file_types = ['bin','dmg','iso','toast','vcd']

# Destination file paths
audio_file_path = 'D:\Downloads\Media\Audio'
image_file_path = 'D:\Downloads\Media\Images'
video_file_path = 'D:\Downloads\Media\Videos'
docs_file_path = 'D:\Downloads\Documents\Docs'
pdf_file_path = 'D:\Downloads\Documents\PDFs'
ppt_file_path = 'D:\Downloads\Documents\PPTs'
spreadsheet_file_path = 'D:\Downloads\Documents\Spreadsheets'
text_file_path = 'D:\Downloads\Documents\Text Files'
compressed_file_path = 'D:\Downloads\Compressed Files\Compressed Files'
disc_file_path = 'D:\Downloads\Compressed Files\Disc Files'
executable_file_path = 'D:\Downloads\Executables'

# Transfer function
def transfer_file(source_path,destination_path):
    shutil.move(source_path,destination_path)
    print(source_path + '>>>' + destination_path)

# Create a loop
for file in files:
    print(i)
    source_path = file_path + '/' + file
    filetype = file.split('.')[1] 
    if filetype in media_file_types:
        if filetype in image_file_types:
            transfer_file(source_path,image_file_path)
        elif filetype in video_file_types:
            transfer_file(source_path,video_file_path)
        elif filetype in audio_file_types:
            transfer_file(source_path,audio_file_path)
    elif filetype in document_file_types:
        if filetype in docs_file_types:
            transfer_file(source_path,docs_file_path)
        elif filetype in pdf_file_types:
            transfer_file(source_path,pdf_file_path)
        elif filetype in ppt_file_types:
            transfer_file(source_path,ppt_file_path)
        elif filetype in spreadsheet_file_types:
            transfer_file(source_path,spreadsheet_file_path)
        elif filetype in text_file_types:
            transfer_file(source_path,text_file_path)
    elif filetype in compresseddisc_file_types:
        if filetype in compressed_file_types:
            transfer_file(source_path,compressed_file_path)
        elif filetype in disc_file_types:
            transfer_file(source_path,disc_file_path)
    elif filetype in executable_file_types:
        transfer_file(source_path,executable_file_path)
    else:
        pass
    i += 1


