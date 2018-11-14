vowels = ['a', 'e', 'i', 'o', 'u']
word = input("Please type your favorite word: ")
found = []
for letter in word:
    if letter in vowels:
        if letter not in found:
            found.append(letter)
for vowels in found:
    print(letter)
print(found)
print(vowels)
