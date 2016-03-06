# -*- coding: utf-8 -*-
import zipfile
import time

__author__ = 'lihui'


# 9-22
def show_zip_info(filename):
    f = zipfile.ZipFile(filename)

    for file in f.namelist():
        info = f.getinfo(file)
        print "Name: %s" % info.filename
        size = info.compress_size
        print "Size: %s" % size
        print "Compression Rate: %s" % round(float(size) / info.file_size, 2)
        time_tuple = info.date_time + (time.localtime()[6:])
        print "Time: %s\n" % time.asctime(time_tuple)



if __name__ == "__main__":
    show_zip_info()