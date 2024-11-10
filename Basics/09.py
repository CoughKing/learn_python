# Modes for file handling: Read, Write, Append

file = open('myfile.txt', 'r')
file.close() #Manully close the file after opening it.

with open('file.txt', 'r') as f:
    
    content = f.read() # Read the entire file
    
print(content)

with open('file.txt', 'w') as f:
    
    f.write('This is a new content.') # Overwrite the existing content

# print(content)    

with open('file.txt', 'a') as f:
    content = f.write('This is a new appended content.')
from os import *

mkdir("file_handling")
chdir("file_handling")

rename("file.txt", "myfile.txt")

remove('myfile.txt')
rmdir("file_handling")