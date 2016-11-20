  This program allows you to watermark all images in a given folder. It allows you to import a photo as your desired watermark
then the image path would be saved to a text file that way the next time the program runs your watermark is saved, and you would
not need to reimport the watermark. You then select a folder you wish your images to be pulled from. The program then creates a
folder named "watermarked_images" that the images will be "saved" to. The program then runs watermarking all images that are
.png, .jpg, or .jpeg in the folder that were selected. These copies are then saved to source folder, which will then be moved into
the "watermarked_images" folder. 


The image manipulation is done using pillow, and the GUI is using tkinter.
The program was written and tested on a chromebook running ubuntu (via crouton)
