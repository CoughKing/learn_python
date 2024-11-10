# Dictionary has key value pairs instead of index.

person = {'name': 'birat', 'age':32, 'gender': 'male'}

print(person['age']) # these keys need to be unique

person['city'] = 'sadarmukam' # adding a new key-value pair\

print(person)

#its method: Items, keys, and values

print(person.items()) # returns a list of tuples, each containing a key-value pair

print(person.keys()) # returns a list of keys

print(person.values()) # returns a list of values