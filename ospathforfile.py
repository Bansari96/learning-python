#Example with file for working with os.path module

import os
from os import path
import datetime
from datetime import date,time,timedelta
import time

def main():
    print(os.name)

    print("Item exist: "+str(path.exists("txtfile.txt")))
    print("Item is file: "+str(path.isfile("txtfile.txt")))
    print("Item is dir: "+str(path.isdir("txtfile.txt")))

    print("Item path: "+str(path.realpath("txtfile.txt")))
    print("Item path and name: "+str(path.split(path.realpath("txtfile.txt"))))

    t=time.ctime(path.getmtime("txtfile.txt"))
    print(t)
    print(datetime.datetime.fromtimestamp(path.getmtime("txtfile.txt")))

    td=datetime.datetime.now()-datetime.datetime.fromtimestamp(
        path.getmtime("txtfile.txt")
    )
    print("It has been "+str(td)+" since the file was modified")
    print("Or, "+str(td.total_seconds())+" seconds")

if __name__ == "__main__":
    main()