"""
Given a string, return the index of its first unique character. 
If a unique character does not exist, return '-1'.

Ex: Given the following strings...

"abcabd", return 2
"thedailybyte", return 1
"developer", return 0
"""

from collections import defaultdict


def first_unique(s: str) -> int:
    tracker = defaultdict(int)
    for c in s:
        tracker[c] += 1
    for k, v in tracker.items():
        if v == 1:
            return s.index(k)
    return -1


if __name__ == "__main__":
    # some edge cases
    print(first_unique(""))
    print(first_unique("a"))
    print(first_unique("cc"))
    # defined cases
    print(first_unique("abcabd"))
    print(first_unique("thedailybyte"))
    print(first_unique("developer"))


# Brute Force approach

# checked = []
# for i, c in enumerate(s):
#     if c not in s[i+1:] and c not in checked:
#         return i
#     checked.append(c)
# return -1
