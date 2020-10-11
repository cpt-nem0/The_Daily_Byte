"""
Given a string, return whether or not it uses capitalization correctly.
A string correctly uses capitalization if all letters are capitalized, 
no letters are capitalized, or only the first letter is capitalized.

Ex: Given the following strings...

"USA", return true
"Calvin", return true
"compUter", return false
"coding", return true
"""


def correct_cap(word):
    count = 0
    for c in word:
        if c.isupper():
            count += 1
        
    return count == 0 or count == len(word) or (count == 1 and word[0].isupper())


if __name__ == "__main__":
    word = input('> ')
    print(correct_cap(word))
