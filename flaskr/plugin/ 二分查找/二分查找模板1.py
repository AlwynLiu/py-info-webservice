#!/usr/bin/python3
# -*- coding: UTF-8 -*-
__Author__ = "Alvin Liu"


def binarySearch(nums, target):
    """
    :type nums: List[int]
    :type target: int
    :rtype: int
    """
    if len(nums) == 0:
        return -1

    left, right = 0, len(nums) - 1
    while left <= right:
        mid = (left + right) // 2
        if nums[mid] == target:
            return mid
        elif nums[mid] < target:
            left = mid + 1
        else:
            right = mid - 1

    # End Condition: left > right
    return -1


# class Solution:
#     def guessNumber(self, n: int) -> int:
#         if n == 1:
#             return 1
#         left, right = 1, n
#         while left <= right:
#             mid = left + int((right - left) / 2)
#             if guess(mid) == 0:
#                 return mid
#             elif guess(mid) == -1:
#                 left = mid + 1
#             else:
#                 right = mid - 1
#
#
# def guess(num):
#     if num
print(6 + 1//2)
