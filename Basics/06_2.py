# Tuples. They are immutable i.e cant replace or change the value at said index

y = (1,2,3) # Tuples cant be sort.

x = list(y) # Tuples can be type casted into list

x[0] = 10

y = tuple(x) # List can be type casted into tuple

print(y)