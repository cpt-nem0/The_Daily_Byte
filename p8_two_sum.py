"""
Given an array of integers, return whether or not two numbers sum to a given target, 'k'.
Note: you may not sum a number with itself.

Ex: Given the following...

[1, 3, 8, 2], k = 10, return true (8 + 2)
[3, 9, 13, 7], k = 8, return false
[4, 2, 6, 5, 2], k = 4, return true (2 + 2)
"""
from typing import List


def twoSum(nums: List, k: int) -> bool:
    tracked_num = {}
    for i, n in enumerate(nums):
        if k-n in tracked_num:
            return True
        tracked_num[n] = i
    return False


if __name__ == "__main__":
    print(twoSum([1, 3, 8, 2], k=10))
    print(twoSum([3, 9, 13, 7], k=8))
    print(twoSum([4, 2, 6, 5, 2], k=4))
