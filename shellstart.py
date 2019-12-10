# Example of file for working with filesystem shell methods

import os
from os import path
import shutil
from shutil import make_archive
from zipfile import ZipFile

def main():
    if path.exists("txtfile.txt"):
        src=path.realpath("txtfile.txt")

        dst=src+".bak"

        #shutil.copy(src,dst)
        #shutil.copystat(src,dst)
       
       #rename file
       #os.name("txtfile.txt","newfile.txt")

       #put everything into ZIP archive
        root_dir, tail=path.split(src)
        shutil.make_archive("archive","zip",root_dir)

       #more fine-grained control over ZIP files
        with ZipFile("testzip.zip","w") as newzip:
           newzip.write("txtfile.txt")
           newzip.write("txtfile.txt.bak")

if __name__ == "__main__":
    main()