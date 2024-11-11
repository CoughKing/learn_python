phrase = "Don't Panic"

plist = list(phrase)


print(plist)
print(phrase)

new_phrase = ''.join(plist[1:3]) #stringify
new_phrase = new_phrase + ''.join([plist[5], plist[4],plist[7], plist[6]])

print(plist)
print(new_phrase)