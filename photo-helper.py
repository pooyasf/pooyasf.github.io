'''
Generate divs and filtering tags based on image names and place them inside a html file.
'''

import sys
import os

photo_folder_path = './Photos/'

directory = os.fsencode(photo_folder_path)
    
for file in os.listdir(directory):
    filename = os.fsdecode(file)
    if filename.endswith(".jpg") or filename.endswith(".png"): 
        print('file name is:',filename)
        continue
    else:
        continue