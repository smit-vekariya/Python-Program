#89 video in code with harry
"""The OS module in Python provides functions for interacting with the operating system. OS comes under Python’s standard utility modules. 
This module provides a portable way of using operating system-dependent functionality.
 The *os* and *os.path* modules include many functions to interact with the file system.
"""

import os

def soldier(path,file,format):

    os.chdir(path)
    files=os.listdir(path)
    #print(files)
    with open(file) as f:
        filelist=f.read().split("\n")
    i=0
    for file in files:
        if file not in filelist:
            os.rename(file,file.capitalize())
        
        if os.path.splitext(file)[1]==format:
            os.rename(file, f"{i}{format}")
            i +=1

soldier(r"S:\Python\EX8",
        r"S:\Python\EX8\ex8.txt",".png")

    

"""os.path.splitext() method in Python is used to split the path name into a pair root and ext.
Here, ext stands for extension 
and has the extension portion of the specified path while root is everything except ext part.
ext is empty if specified path does not have any extension. If the specified path has leading period (‘.’),
it will be ignored.

For example consider the following path names:

      path name                          root                        ext
/home/User/Desktop/file.txt    /home/User/Desktop/file              .txt
/home/User/Desktop             /home/User/Desktop                  {empty}"""
