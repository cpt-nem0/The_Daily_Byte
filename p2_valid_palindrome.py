"""
Given a string, return whether or not it forms a palindrome ignoring case and non-alphabetical characters.
Note: a palindrome is a sequence of characters that reads the same forwards and backwards.

Ex: Given the following strings...

"level", return true
"algorithm", return false
"A man, a plan, a canal: Panama.", return true
"""


def valid_palin(s):
    l, r = 0, len(s)-1

    while(l < r):

        while(l < r and not(s[l].isalpha())):
            l += 1
        while(l < r and not(s[r].isalpha())):
            r -= 1

        if s[l] == s[r]:
            l += 1
            r -= 1
        else:
            return False

    return True


if __name__ == "__main__":
    s = input('> ').lower()
    print(valid_palin(s))


# 2nd solution
# s = input('> ').lower()
# ns = ''.join([i for i in s if i.isalpha()])
# print(ns == ns[::-1])
