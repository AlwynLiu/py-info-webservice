#!/usr/bin/python3
# -*- coding: UTF-8 -*-
__Author__ = "Alvin Liu"


from typing import List


class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        left = 0
        print("k:", k)
        for j in range(0, k - 1):
            for i in range(0, len(nums) - 1):
                if nums[left] <= nums[i] and j < i:
                    nums[left], nums[i] = nums[i], nums[left]
                    print('nums[left]:', i, left)
                    left += 1
            print('numsssss:', nums[j])
        return j
    
    
print(Solution().findKthLargest([3, 2, 3, 1, 2, 4, 5, 5, 6], 4))