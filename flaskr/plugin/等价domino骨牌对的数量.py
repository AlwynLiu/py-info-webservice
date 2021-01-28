#!/usr/bin/python3
# -*- coding: UTF-8 -*-
__Author__ = "Alvin Liu"

from typing import List


class Solution:
    def numEquivDominoPairs(self, dominoes: List[List[int]]) -> int:
        # 生成100个0的num数组
        num = [0] * 100
        ret = 0
        for x, y in dominoes:
            val = (x * 10 + y if x <= y else y * 10 + x)
            print('val:', val)
            ret += num[val]
            num[val] += 1
            print('num', num)
            print('num[val]:', num[val], ',,,,,ret:', ret)
        return ret



print(Solution().numEquivDominoPairs([[7, 8], [7,8], [7,8],[1,2],[1,2],[7,8]]))
