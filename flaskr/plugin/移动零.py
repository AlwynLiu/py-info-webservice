# -*- coding: utf-8 -*-
"""
@Author ： Alvin.Liu
"""


from typing import List


nums = [2, 1, 3, 0, 4, 0, 8, 0]

class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        n = len(nums)
        left = right = 0
        while right < n:
            if nums[right] != 0:
                nums[left], nums[right] = nums[right], nums[left]
                left += 1
            right += 1