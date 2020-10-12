"""
You are given two strings, 's' and 't' which only consist of lowercase letters. 
't' is generated by shuffling the letters in 's' as well as potentially adding 
an additional random character. Return the letter that was randomly added 
to 't' if it exists, otherwise, return ''.
Note: You may assume that at most one additional character can be added to 't'.

Ex: Given the following strings...

s = "foobar", t = "barfoot", return 't'
s = "ide", t = "idea", return 'a'
s = "coding", t "ingcod", return ''
"""

from collections import defaultdict


def spotDifference(s: str, t: str) -> str:
    res = ''
    t_map = defaultdict(int)
    for c in t:
        t_map[c] += 1
    for c in s:
        t_map[c] -= 1
    for k, v in t_map.items():
        if v == 1:
            res += k
            break
    return res


if __name__ == "__main__":
    print(spotDifference(s="a", t="aa"))
    print(spotDifference(s="foobar", t="barfoot"))
    print(spotDifference(s="ide", t="idea"))
    print(spotDifference(s="coding", t="ingcod"))
