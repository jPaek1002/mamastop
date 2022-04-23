import os
from tkinter import *
from tkinter import filedialog
from os import path
from os import listdir
from PIL import Image, ImageTk

class da_croppa:
    def __init__(self):
        self.root = Tk()
        self.root.title("Image viewer application using python")
        self.root.resizable(0, 0)
        # create frame
        self.frame=Frame(self.root, width=600, height=500, bg='white', relief=GROOVE, bd=2)
        self.frame.pack(padx=10, pady=10)
        self.images = []
        self.image_label = None
        self.dirname = None
        self.dirpath = None

    def select_in_folder(self):
        self.dirname = filedialog.askdirectory()
        if self.dirname is not None:
            self.get_images(self.dirname)


    def get_images(self, dirname):
        self.dirpath = os.path.abspath(dirname)
        fnames = [os.path.join(os.path.abspath(self.dirpath), x) for x in listdir(self.dirpath)]
        for fname in fnames:
    # create thumbanials of all images
    img1 = Image.open('img1.jpg')
    img1.thumbnail((550, 450))
    img2 = Image.open('img2.jpg')
    img2.thumbnail((550, 450))
    img3 = Image.open('img3.jpg')
    img3.thumbnail((550, 450))
    img4 = Image.open('img4.jpg')
    img4.thumbnail((550, 450))
    img5 = Image.open('img5.jpg')
    img5.thumbnail((550, 450))
    # open images to use with labels
    image1 = ImageTk.PhotoImage(img1)
    image2 = ImageTk.PhotoImage(img2)
    image3 = ImageTk.PhotoImage(img3)
    image4 = ImageTk.PhotoImage(img4)
    image5 = ImageTk.PhotoImage(img5)
    # create list of images
    images = [image1, image2, image3, image4, image5]
    # configure the image to the Label in frame
    i = 0
    image_label = Label(frame, image=images[i])
    image_label.pack()
    # create functions to display
    # previous an next images


    def launch(self):
        def previous():
            global i
            i = i - 1
            try:
                image_label.config(image=images[i])
            except:
                i = 0
                previous()

        def next():
            global i
            i = i + 1
            try:
                image_label.config(image=images[i])
            except:
                i = -1
                next()
        # create buttons
        btn1 = Button(self.root, text="Previous", bg='black', fg='gold', font=('ariel 15 bold'), relief=GROOVE, command=previous)
        btn1.pack(side=LEFT, padx=60, pady=5)
        btn2 = Button(self.root, text="Next", width=8, bg='black', fg='gold', font=('ariel 15 bold'), relief=GROOVE, command=next)
        btn2.pack(side=LEFT, padx=60, pady=5)
        btn3 = Button(self.root, text="Exit", width=8, bg='black', fg='gold', font=('ariel 15 bold'), relief=GROOVE, command=root.destroy)
        btn3.pack(side=LEFT, padx=60, pady=5)
        in_folder = Button(window,
                           text="Select Input Files",
                           command=select_in_folder)
        self.root.mainloop()