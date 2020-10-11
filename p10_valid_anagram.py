"""
Given two strings 's' and 't' return whether or not 's' is an anagram of 't'.
Note: An anagram is a word formed by reordering the letters of another word.

Ex: Given the following strings...

s = "cat", t = "tac", return true
s = "cat", t = "tac", return true
s = "program", t = "function", return false
"""


def valid_anagram(s: str, t: str) -> bool:

    if len(s) != len(t):
        return False

    s_map = {}
    t_map = {}
    for char in t:
        if char in t_map:
            t_map[char] += 1

        else:
            t_map[char] = 1
    for char in s:
        if char in s_map:
            s_map[char] += 1

        else:
            s_map[char] = 1

    return s_map == t_map


if __name__ == "__main__":
    print(valid_anagram(s="cat", t="tac"))
    print(valid_anagram(s="cat", t="tac"))
    print(valid_anagram(s="program", t="function"))


# alternative

# from collections import defaultdict
# tracker = defaultdict(int)
# for c in t:
#     tracker[c] += 1
# for c in s:
#     tracker[c] -= 1

# return all(res == 0 for res in tracker.values())
