from Tkinter import *
from tkFileDialog import askopenfilename
import sys
from PIL import Image

photo_path = ""
remembered_file = 'watermarker_remembered_path.txt'

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


def watermark_files():
    watermark_path = open(remembered_file, 'r').read()
    watermark_image = Image.open(watermark_path)
    queued_image = Image.open(photo_path)
    print('do all the things')

#main tk window
root = Tk()
root.title('Watermarker')
root.geometry('360x200')

select_label = Label(root, text = "Please import the file you wish to watermark").grid(row = 0)
import_button = Button(root, text = "Import", command = lambda root = root:set_photo_path()).grid(row = 1)

watermarker_label = Label(root, text = "Select your watermark").grid(row = 2)
select_button = Button(root, text = "Select", command = lambda root = root:import_watermark_path()).grid(row = 3)
reminder_label = Label(root, text = "Reminder: Your last used watermark will be saved for reuse").grid(row = 4)
watermarker = Button(root, text = 'Watermark', command = lambda root = root: watermark_files()).grid(row = 5)

cancel_button = Button(root, text = "Cancel", command = lambda root = root:sys.exit()).grid(row = 6)


#end of tkinter
root.mainloop()