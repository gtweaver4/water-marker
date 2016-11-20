from Tkinter import *
from tkFileDialog import askopenfilename
from tkFileDialog import askdirectory
import sys
from PIL import Image
import os
import shutil

photo_path = ""
remembered_file = 'watermarker_remembered_path.txt'

def watermark_folder():
    global photo_path
    files = os.listdir(photo_path)
    if not os.path.exists(photo_path + "/watermarked_images"):
        os.mkdir(photo_path + '/watermarked_images')
    for f in files:
        watermark_file((photo_path + "/" + f))

    move_files()
    print('completed')
    sys.exit()


def ask_directory():
    #returns a selected directory
    global photo_path 
    photo_path = askdirectory()

#creates the file selector GUI
def file_selector():
    return askopenfilename()

#setting photo photo_path
def set_photo_path():
    global photo_path
    photo_path = file_selector()

#imports and saves watermark location
def import_watermark_path():
    #since not using append it clears file automatically
    f = open(remembered_file, 'w')
    tmp_path = file_selector()
    if(tmp_path.endswith('.jpg') or tmp_path.endswith('.jpeg') or tmp_path.endswith('.png')):
        f.write(tmp_path)
        f.close()
    else:
        print('Please select a .JPG, .JPEG, or .PNG image')

def move_files():
    global photo_path
    source_folder = os.getcwd()
    destination_folder = photo_path + "/watermarked_images"
    #if not os.path.exists(destination_folder):
        #os.mkdir(destination_folder, 0755)

    files = os.listdir(source_folder)

    for f in files:
        if(f.endswith('.jpg') or f.endswith('jpeg') or f.endswith('png')):
            full_path = source_folder + "/" + f
            shutil.move(full_path , destination_folder)


def watermark_file(file_path):
    watermark_path = open(remembered_file, 'r').read()
    watermark_image = Image.open(watermark_path)
    watermark_width, watermark_height = watermark_image.size
    queued_image = Image.open(file_path)
    queue_width, queue_height = queued_image.size
    queued_image.paste(watermark_image, (queue_width-watermark_width, queue_height-watermark_height))
    split = file_path.split('/')
    queued_image.save(split[-1])

#main tk window
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