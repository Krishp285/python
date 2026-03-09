string = input("Enter a string: ").upper()
for i in string:
    if i in "AEIOU":
        with open("vowels.txt", "a") as vowel_file:
            vowel_file.write(i + "\n")
    else:
        with open("consonants.txt", "a") as consonant_file:
            consonant_file.write(i + "\n")