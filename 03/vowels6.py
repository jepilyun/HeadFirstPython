vowels = ['a', 'e', 'i', 'o', 'u']
word = input("Provide a word to search for vowels: ")
found = {}

for x in vowels:
    found.setdefault(x, 0)

for letter in word:
    if letter in vowels:
        found[letter] += 1

for k, v in found.items():
    if v > 0:
        print(k, 'was found', v, 'time(s).')
