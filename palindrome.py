print("This code verifies if the captured word is a Palindrome.")
word = input("Give me the word to analize: ").lower()

# This is a slice. It indicates to start at the end of the string and move backwards by a step of -1. This reverses
# the string.
reversedWord = word[::-1]

if word == reversedWord:
    print(f"The word '{word}' is a palindrome.")
else:
    print(f"The word '{word}' is not a palindrome.")