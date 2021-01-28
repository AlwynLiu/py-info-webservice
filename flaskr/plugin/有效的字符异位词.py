#!/usr/bin/python3
# -*- coding: UTF-8 -*-
__Author__ = "Alvin Liu"

class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) == len(t):
            if len(s) > 1:
                SArray = list(s)
                SArray.sort()
                TArray = list(t)
                TArray.sort()
                if SArray == TArray:
                    return True
                else:
                    return False
            else:
                if s == t:
                    return True
                else:
                    return False
        else:
            return False


print(Solution().isAnagram('ab', 'ba'))
