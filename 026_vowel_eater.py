# "Eat" the vowels of a given word and display only its consonants

user_word = str(input("Enter a word: "))
user_word = user_word.upper()

for letter in user_word:
    if letter == "A":
        continue
    if letter == "E":
        continue
    if letter == "I":
        continue
    if letter == "O":
        continue
    if letter == "U":
        continue
    else:
        print(letter)