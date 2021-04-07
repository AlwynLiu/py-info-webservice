#!/usr/bin/python3
# -*- coding: UTF-8 -*-
__Author__ = "Alvin Liu"

class Solution:
    def isPalindrome(self, s: str) -> bool:
        """
        空字符串，ch.lower,
        这写法666，
        :param s:
        :return:
        """
        sgood = "".join(ch.lower() for ch in s if ch.isalnum())
        return sgood == sgood[::-1]


str1 = 'Hello world, I\'m haha '
# lowerString = str1.lower()
# for ch in lowerString:
#     if ch.isalnum():
#         print(ch)

print("".join(ch.lower() for ch in str1 if ch.isalnum()))
