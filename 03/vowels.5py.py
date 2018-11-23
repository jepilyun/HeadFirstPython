vowels = ['a', 'e', 'i', 'o', 'u']
word = input("Provide a word to search for vowels: ")
found = {}

found.setdefault('a', 0)
found.setdefault('e', 0)
found.setdefault('i', 0)
found.setdefault('o', 0)
found.setdefault('u', 0)

for letter in word:
    if letter in vowels:
        found[letter] += 1

for k, v in found.items():
    if v > 0:
        print(k, 'was found', v, 'time(s).')
