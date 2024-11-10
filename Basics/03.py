# Arithmetic operations +, -, *, /, %, **, //

a=2
b=3

sum = a+b
difference = a-b
mul = a*b
divide = a/b
power = a**b
float_divide = a//b
# print(float_divide)

# Assignemnt operations 

x=10
x += 10  #so on for other arithmetic operation.

# comparison operations ==, !=, <, >, <=, >= and it results in boolean

# print (x>power) and works on Strings too

# Logical operations and, or, not

# User Input

m = input("Enter Something of Your Choice") #stores as a string
n = input("Enter  another Something of Your Choice") 

m = int(m)
n = int(n)

print(m + n)

# membership operations: in, not in

my_list = [1,2,3,4,5]

print(2 in my_list)
print(7 in my_list)

#is, is not are identity operation

h = 10

if type(h) is int:
    print("It's an Integer")
else:
    print("It's not an Integer")