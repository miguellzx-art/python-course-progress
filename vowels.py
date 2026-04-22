text = input("Enter a phrase to count vowels and consonants: ")
vowels = "aeiouAEIOU"
consonants = "bcdfghjklmnpqrstvwxyzBCDFGHJKLMNPQRSTVWXYZ"
num_vowels = 0
num_consonants = 0

for letter in text:
    if letter in vowels:
        num_vowels += 1
    elif letter in consonants:
        num_consonants += 1

print(f"The phrase contains {num_vowels} vowels and {num_consonants} consonants.")