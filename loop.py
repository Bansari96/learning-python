# Example for loops in python

def main():
    x=0

    # while loop
    while(x<5):
        print(x)
        x=x+1
    # for loop
    for x in range(1,10):  #in the range 10 is not inclusive, it will not print 10
        print(x)

    #for loop over collection
    days=["Mon","Tue","Wed"]
    for d in days:
        print(d)

    # for loop with break continue statements
    for x in range(5,10):
        #if(x==7):break
        if (x%2==0):continue
        print(x)

    # using the enumerate() function to get index
    days=["Mon","Tue","Wed"]
    for i,d in enumerate(days):
        print(i,d) #returns index with day value (eg: 0 Mon)


if __name__=="__main__":
    main()