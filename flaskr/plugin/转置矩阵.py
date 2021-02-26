#!/usr/bin/python3
# -*- coding: UTF-8 -*-
__Author__ = "Alvin Liu"

# 力扣 867. 转置矩阵
from typing import List

class Solution:
    def transpose(self, matrix: List[List[int]]) -> List[List[int]]:
        m, n = len(matrix), len(matrix[0])
        
        transposed = [[0] * m for _ in range(n)]
        for i in range(m):
            for j in range(n):
                transposed[j][i] = matrix[i][j]
        return transposed
    
    
Solution().transpose([[1, 2], [3, 4]])
