# !/usr/bin/env Python3
# -*- coding: utf-8 -*-

#  @Author: Frenude 
#  @Description:
#  @Date: Created in 01 06,2021
#  @Modified By:

class SolutionByViolent:
    def lengthOfLongestSubstring(self, s: str) -> int:
        if not len(s):
            return 0
        max_l = 0
        for i in range(len(s)):
            str_set = set()
            l = 0
            for j in range(i,len(s)):
                if s[j] in str_set:
                    break
                str_set.add(s[j])
                l += 1
            max_l = max(l,max_l)
        return max_l
if __name__ == '__main__':
    s = "pwwkew"
    so = SolutionByViolent()
    z = so.lengthOfLongestSubstring(s)
    print(z)
