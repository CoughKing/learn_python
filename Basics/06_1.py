# Lists and its Functions: len. max, min and its Method: append, insert, remove, pop, .index, sort

mylist = [10, 20.45, 30, "this python", True, "Dat"]

print (mylist[3:5])

mylist[3] = "haha lulz"

print (mylist[3])

for x in mylist:
    print(x)

nextlist = [1,2,3,4,5,6]

for y in nextlist:
    print (y ** 3)

print (mylist + nextlist)

print (nextlist * 4) # it repeats the list

print (min(nextlist))

nextlist.append(7) #add at last
print (nextlist)

mylist.insert(2, "Hello") #any specific location
print(mylist)

nextlist.remove(7) #remove that mentioned element (value)
print(nextlist)

mylist.pop(2) #remobe at location without knowing the value
print(mylist)

print(nextlist.index(5)) #prints the index of said value

# mylist.pop(mylist.index("Hello")) 

random = [45,67,12,45,32,6,2,87]

random.sort() #sort in ascending order

print(random) #print(sorted(random)) keeping the unsorted list without changin it