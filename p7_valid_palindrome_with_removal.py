"""
Given a string and the ability to delete at most one character,
return whether or not it can form a palindrome.
Note: a palindrome is a sequence of characters that reads the same forwards and backwards.

Ex: Given the following strings...

"abcba", return true
"foobof", return true (remove the first 'o', the second 'o', or 'b')
"abccab", return false
"""


def isPalin(s, i, j):
    while(i < j):
        if s[i] != s[j]:
            return False
        i += 1
        j -= 1
    return True


def validPalin(s):
    i, j = 0, len(s)-1
    while(i < j):
        if s[i] == s[j]:
            i += 1
            j -= 1
        else:
            return isPalin(s, i+1, j) or isPalin(s, i, j-1)

    return True


if __name__ == "__main__":
    print(validPalin("abcba"))
    print(validPalin("foobof"))
    print(validPalin("abccab"))
