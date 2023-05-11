import os
import os.path as path
from glob import glob

from PIL import Image

sourcedir = path.abspath('Photos')
destdir = path.abspath('thumbnails')


def main():
    files = glob(path.join(sourcedir, '*.png'))

    for imgfile in files:
        destpath = path.join(destdir, imgfile)
        image = Image.open(imgfile)
        current_width, current_height = image.size
        new_width = current_width // 4
        new_height = current_height // 4
        new_size = (new_width, new_height)
        image.thumbnail(new_size)
        image.save(destpath)


if __name__ == '__main__':
    main()
