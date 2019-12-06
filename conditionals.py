# Example for Conditional Structures in python

def main():
    x,y=10,110

    if(x<y):
        st="x is less than y"
    elif(x==y):
        st="x is equeal to y"
    else:
        st="x is greater than y"
    print(st)

#using conditional statements
st="x is less than y" if (x<y) else "x is greater than or equal to y"

print(st)

if __name__=="__main__":
    main()