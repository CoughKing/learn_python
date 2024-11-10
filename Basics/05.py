# While Loop: It continues until the certain condition are satisfied


# x = 0

# while x < 10:
#     # print(x)
#     x += 1
    
# # For loop iteration:

# for y in range(21):
#     # print(y) # from 0 to 20

# for z in range(5,15):
#     # print(z) # from 5 to 14


x = 0

while x < 10:
    # if x == 5:
    #     break #stops the loop from there
    x += 1
    if x == 5:
        continue # skips that one iteration
    print(x)

if x == 25:
    pass # lets the interpreter to run through more code