# Handling The error Message.

try:
    x= int(input("First Number:"))
    y= int(input("Second Number:"))
    print(x/y)
except ValueError:
    print("Please Enter a Valid Number")
except ZeroDivisionError:
    print("Cannot Divide by Zero. Enter a Number") 
    y = 1
    print(x/y)   

finally:
    print("Ok Done!")  


# Rasising A Exception

def some_function():
    if True:
        raise ValueError("Something went terribly Wrong")
    
some_function()


x= 100
y= 20

assert(x<y)