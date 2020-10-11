"""
Given a string representing your stones and another string representing 
a list of jewels, return the number of stones that you have that are also 
jewels.

Ex: Given the following jewels and stones...

jewels = "abc", stones = "ac", return 2
jewels = "Af", stones = "AaaddfFf", return 3
jewels = "AYOPD", stones = "ayopd", return 0
"""


def jewels_and_stone(jewels: str, stones: str) -> int:
    stone_map = {}
    for stone in stones:
        if stone in stone_map:
            stone_map[stone] += 1
        else:
            stone_map[stone] = 1
    res = 0
    for jewel in set(jewels):
        if jewel in stone_map:
            res += stone_map[jewel]

    return res


if __name__ == "__main__":
    print(jewels_and_stone("abc", "ac"))
    print(jewels_and_stone("Af", "AaaddfFf"))
    print(jewels_and_stone("AYOPD", "ayopd"))
