"""
Given an array of strings, return the longest common prefix that is shared amongst all strings.
Note: you may assume all strings only contain lowercase alphabetical characters.

Ex: Given the following arrays...

["colorado", "color", "cold"], return "col"
["a", "b", "c"], return ""
["spot", "spotty", "spotted"], return "spot"
"""


def longestCommonPrefix(strs):
    longestPrefix = ''

    if not len(strs):
        return longestPrefix
    j = 0
    for c in strs[0]:
        for i in range(1, len(strs)):
            if (j >= len(strs[i])) or (c != strs[i][j]):
                return longestPrefix
        j += 1
        longestPrefix += c

    return longestPrefix


if __name__ == "__main__":
    # strs = input().split()
    print(longestCommonPrefix(["colorado", "color", "cold"]))
    print(longestCommonPrefix(["a", "b", "c"]))
    print(longestCommonPrefix(["spot", "spotty", "spotted"]))
