from Tkinter import *
from tkFileDialog import askopenfilename
from tkFileDialog import askdirectory
from PIL import Image
import sys
import os
import shutil

#created these variables to be global
folder_path = ""
remembered_file = 'watermarker_remembered_path.txt'

#watermarks entire folder and creates a directory
#if directory doesnt already exist
def watermark_folder():
    global folder_path
    files = os.listdir(folder_path)
    if not os.path.exists(folder_path + "/watermarked_images"):
        os.mkdir(folder_path + '/watermarked_images')
    for f in files:
        watermark_file((folder_path + "/" + f))

    move_files()
    print('completed')
    sys.exit()

#gets a directory to set as the folder_path
def ask_directory():
    global folder_path 
    folder_path = askdirectory()

#creates the file selector GUI
def file_selector():
    return askopenfilename()

#imports and saves watermark location
#into txt file
def import_watermark_path():
    #since not using append it clears file automatically
    f = open(remembered_file, 'w')
    tmp_path = file_selector()
    if(tmp_path.endswith('.jpg') or tmp_path.endswith('.jpeg') or tmp_path.endswith('.png')):
        f.write(tmp_path)
        f.close()
    else:
        print('Please select a .JPG, .JPEG, or .PNG image')

#moves files from the source directory to the location of the photo imports
#this relies on the watermarked_images folder to have been created
def move_files():
    global folder_path
    source_folder = os.getcwd()
    destination_folder = folder_path + "/watermarked_images"
    files = os.listdir(source_folder)
    for f in files:
        if(f.endswith('.jpg') or f.endswith('jpeg') or f.endswith('png')):
            full_path = source_folder + "/" + f
            shutil.move(full_path , destination_folder)


#this watermarks a singular image
def watermark_file(file_path):
    watermark_path = open(remembered_file, 'r').read()
    watermark_image = Image.open(watermark_path)
    watermark_width, watermark_height = watermark_image.size
    queued_image = Image.open(file_path)
    queue_width, queue_height = queued_image.size
    queued_image.paste(watermark_image, (queue_width-watermark_width, queue_height-watermark_height))
    split = file_path.split('/')
    queued_image.save(split[-1])

#main tk window for simple GUI
root = Tk()
root.title('Watermarker')
root.geometry('360x200')

select_label = Label(root, text = "Please import the folder you wish to watermark").grid(row = 0)
import_button = Button(root, text = "Import", command = lambda root = root:ask_directory()).grid(row = 1)
watermarker_label = Label(root, text = "Select your watermark").grid(row = 2)
select_button = Button(root, text = "Select", command = lambda root = root:import_watermark_path()).grid(row = 3)
reminder_label = Label(root, text = "Reminder: Your last used watermark will be saved for reuse").grid(row = 4)
watermarker = Button(root, text = 'Process', command = lambda root = root: watermark_folder()).grid(row = 5)
cancel_button = Button(root, text = "Cancel", command = lambda root = root:sys.exit()).grid(row = 6)

#end of tkinter
root.mainloop()