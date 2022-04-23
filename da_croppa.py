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
        self.frame = Frame(self.root, width=600, height=500, bg='white', relief=GROOVE, bd=2)
        self.frame.pack(padx=10, pady=10)
        self.images = [ImageTk.PhotoImage(Image.open('welcome.jpg'))]
        self.image_label = None
        self.dirname = None
        self.dirpath = None
        self.page = 0

    def select_in_folder(self):
        self.dirname = filedialog.askdirectory()
        if self.dirname is not None:
            self.get_images(self.dirname)

    def get_images(self, dirname):
        self.dirpath = os.path.abspath(dirname)
        fnames = [os.path.join(os.path.abspath(self.dirpath), x) for x in listdir(self.dirpath)]
        for fname in fnames:
            print(fname)
            file_ext = os.path.splitext(fname)[1][1:]
            if file_ext in ["jpg", "png", "PNG", "tif", "jpeg", "JPG", "JPEG", "jfif"]:
                img = Image.open(fname)
                img.thumbnail((450,800))
                self.images.append(ImageTk.PhotoImage(img))

    def launch(self):
        self.image_label = Label(self.frame, image=self.images[self.page])
        self.image_label.pack()

        def previous():
            self.page -= 1
            try:
                self.image_label.config(image=self.images[self.page])
            except:
                self.page = 0

        def next():
            self.page += 1
            try:
                self.image_label.config(image=self.images[self.page])
            except:
                self.page = -1

        # create buttons
        btn1 = Button(self.root, text="Previous", bg='black', fg='gold', font=('ariel 15 bold'), relief=GROOVE,
                      command=previous)
        btn1.pack(side=LEFT, padx=60, pady=5)
        btn2 = Button(self.root, text="Next", width=8, bg='black', fg='gold', font=('ariel 15 bold'), relief=GROOVE,
                      command=next)
        btn2.pack(side=LEFT, padx=60, pady=5)
        btn3 = Button(self.root, text="Exit", width=8, bg='black', fg='gold', font=('ariel 15 bold'), relief=GROOVE,
                      command=self.root.destroy)
        btn3.pack(side=LEFT, padx=60, pady=5)
        in_folder = Button(self.root, text="Select Input Files", width=8, bg='black', fg='gold', font=('ariel 15 bold'),
                           relief=GROOVE, command=self.select_in_folder())
        in_folder.pack(side=LEFT, padx=60, pady=5)
        self.root.mainloop()
