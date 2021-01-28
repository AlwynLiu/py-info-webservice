#!/usr/bin/python3
# -*- coding: UTF-8 -*-
__Author__ = "Alvin Liu"


from typing import List

class Solution:
    def pivotIndex(self, nums: List[int]) -> int:
        result = -1
        for index, num in enumerate(nums):
            if sum(nums[:index]) == sum(nums[index + 1:]):
                return index
        return result
            
            
            
print(Solution().pivotIndex([1, 7, 3, 6, 5, 6]))