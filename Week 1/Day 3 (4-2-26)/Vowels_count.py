def print_vowels(text):
    vowels = "aeiouAEIOU"

    for char in text:
        if char in vowels:
            print(char)

string=input("Enter the word : ")
print_vowels(string)
