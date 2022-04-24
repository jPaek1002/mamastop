from os import listdir

from mamastop import MaMaStop
from da_croppa import da_croppa
import os

if __name__ == "__main__":
    gui = da_croppa()
    gui.launch()
    # dirname = '80'
    # dirpath = os.path.abspath(dirname)
    # fnames = [os.path.join(os.path.abspath(dirpath), x) for x in listdir(dirpath)]
    # imgs = []
    # for fname in fnames:
    #     print(fname)
