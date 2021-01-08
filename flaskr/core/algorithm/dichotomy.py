from typing import List

# 执行通过
# class Solution:
#     def missingNumber(self, nums: List[int]) -> int:
#         i, j = 0, len(nums) - 1
#         while i <= j:
#             m = (i + j) // 2
#             print(m, i, j)
#             if nums[m] == m:
#                 i = m + 1
#             else:
#                 j = m - 1
#         return i
#
# print(Solution().missingNumber([0]))


# 执行未通过
class Solution:
    def hIndex(self, citations: List[int]) -> int:
        i, j = 0, len(citations) - 1
        num = (i + j) // 2
        if len(citations) - citations[num] <= citations[num]:
            i = num
        else:
            j = num - 1
        print(len(citations))
        return citations[i]



print(Solution().hIndex([0,1,3,5,6,7,19]))