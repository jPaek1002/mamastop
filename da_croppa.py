import os
from tkinter import *
from tkinter import filedialog
from os import path
from os import listdir
from PIL import Image, ImageTk
from mamastop import MaMaStop


class da_croppa:
    def __init__(self):
        self.root = Tk()
        self.root.title("Image viewer application using python")
        self.root.resizable(0, 0)
        # create frame
        self.frame = Frame(self.root, width=300, height=800, bg='white', relief=GROOVE, bd=2)
        self.frame.pack(padx=10, pady=10)
        self.images = [Image.open('welcome.jpg')]
        self.image_label = None
        self.dirname = None
        self.dirpath = None
        self.page = 0
        self.coords1 = None
        self.coords2 = None
        self.reader = MaMaStop()
        self.current = None

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
                img = Image.open(fname).resize((500,800))
                self.images.append(img)

    def get_rect(self):
        if self.coords1 is not None and self.coords2 is not None:
            img = self.images[self.page].crop((min(self.coords1[0],self.coords2[0]),
                                                  min(self.coords1[1], self.coords2[1]),
                                                      max(self.coords1[0], self.coords2[0]),
                                                          max(self.coords1[1], self.coords2[1])))
            img.save('temp.png')
            print(MaMaStop.img_to_string('temp.png', 'temp.png'))
            os.remove('temp.png')
            self.coords1 = None
            self.coords2 = None



    def launch(self):
        self.current = ImageTk.PhotoImage(self.images[self.page])
        self.image_label = Label(self.frame, image=self.current)
        self.image_label.pack()

        def previous():
            self.page -= 1
            self.current = ImageTk.PhotoImage(self.images[self.page])
            try:
                temp = ImageTk.PhotoImage(self.current)
                self.image_label.config(image=temp)
            except:
                self.page = 0

        def next():
            self.page += 1
            self.current = ImageTk.PhotoImage(self.images[self.page])
            try:
                self.image_label.config(image=self.current)
            except:
                self.page = -1

        def select1(event):
            if self.image_label.winfo_x() < event.x < self.image_label.winfo_x() + self.images[self.page].size[0] \
                    and self.image_label.winfo_y() < event.y < self.image_label.winfo_y() + self.images[self.page].size[1]:
                self.coords1 = [event.x - self.image_label.winfo_x(), event.y - self.image_label.winfo_y()]
                print("x")
            self.get_rect()

        def select2(event):
            if self.image_label.winfo_x() < event.x < self.image_label.winfo_x() + self.images[self.page].size[0] \
                    and self.image_label.winfo_y() < event.y < self.image_label.winfo_y() + self.images[self.page].size[1]:
                self.coords2 = [event.x - self.image_label.winfo_x(), event.y - self.image_label.winfo_y()]
                print("y")
            self.get_rect()


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
                           relief=GROOVE, command=lambda: self.select_in_folder())
        in_folder.pack(side=LEFT, padx=60, pady=5)
        self.root.bind("<Button-1>", select1)
        self.root.bind("<Button-2>", select2)

        self.root.mainloop()
