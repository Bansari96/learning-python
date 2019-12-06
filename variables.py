# Example for variables in python

# Declare
f=0
print(f)

# Re-declare
f="abc"
print(f)

# diff variable type
print("This is a string" + str(123))

# global-local variable
f="abc"
def function():
    global f
    f="xyz"
    print(f)

function()
print(f)
#deleting global variable
del f
print(f)

