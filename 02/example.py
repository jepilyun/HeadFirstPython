phrase = "Don't Panic!"
plist = list(phrase)
print(phrase)
print(plist)

for i in range(4):
    plist.pop()
print(plist)
plist.remove("'")
plist.remove("D")
print()
plist.extend([plist.pop(), plist.pop()])
plist.insert(2, plist.pop(3))

new_phrase = ''.join(plist)
print(plist)
print(new_phrase)
