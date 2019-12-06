# Example for classes in python

class myClass():
    def method1(self):
        print("inside method 1 from class 1")
    
    def method2(self,someString):
        print("inside method 2 from class 2"+someString)

class mySecondClass(myClass):
    def method1(self):
        myClass.method1(self)
        print("inside method 1 from class 2")
    
    def method2(self,someString):
        print("inside method 2 from class 2")

def main():
    c=myClass()
    c.method1()
    c.method2(" From string")

    c2=mySecondClass()
    c2.method1()
    c2.method2(" From string")
    
if __name__ == "__main__":
    main()
