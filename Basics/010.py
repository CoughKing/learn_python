# String are sequence just like list so it can use its methods for different purposes.


# text = "Pizza Boy \nHaha Lulz Poor"

# name = input()
# age = input()

# print(f"Hello {name}, you are {age} years old.")

#  Case Manipulation Function




text = "Pizza Boy \nHaha Lulz"

text = text.upper() #upper or lower, Title, Swap
print(text)

#Count Function

text1 = "Hello Missipissi"

print(text1.count("i")) # Counting the number of 'i' in the string


print(text.find("o")) # finds the index of the letters in the string

separator = ';'

mylist = ["Apple", "Banana", "Cherry"]

print(separator.join(mylist)) # joins the list elements with the separator

words = text.split(" ")
print(words) #


# Replace

text2 = "Hello World"

print(text2.replace("World", "Universe")) # replaces the word