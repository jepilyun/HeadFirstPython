word = "bottles"
for bear_num in range(99, 0, -1):
    print(bear_num, word, "of beer on the wall.")
    print(bear_num, word, "of beer.")
    print("Take one down.")
    print("Pass it around.")
    if bear_num == 1:
        print("No more bottles of beer on the wall.")
    else:
        new_num = bear_num - 1
        if new_num == 1:
            word = "bottle"
        print(new_num, word, "of beer on the wall.")
    print()
    
