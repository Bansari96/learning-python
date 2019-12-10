
#Example with file to create,write and read data

def main():
    #open a for writing and create if doesn't have "w+"
    #if=open("txtfile.txt","w+")
    #append data in the file "a"
    f=open("txtfile.txt","a")

    #writing something in the file
    for i in range(10):
        f.write("Line number: " + str(i) + "\r\n")

    f.close()

    #reading the content from file when f=open("txtfile.txt","r")
    if f.mode=='r':
        contents=f.read()
        print(contents)

if __name__ == "__main__":
    main()