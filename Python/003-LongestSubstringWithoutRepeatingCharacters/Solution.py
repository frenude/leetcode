# !/usr/bin/env Python3
# -*- coding: utf-8 -*-

#  @Author: Frenude 
#  @Description:
#  @Date: Created in 01 06,2021
#  @Modified By:

class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        l = -1
        ret = 0
        hashdict = {}
        for i,k in enumerate(s):
            if k in hashdict and hashdict[k] :
                print(hashdict[k],i)
                l = hashdict[k]
                hashdict[k] = i
            else:
                hashdict[k] = i
                ret = max(ret,i-l)
        return ret


if __name__ == '__main__':
    s = "tmmzuxt"
    so = Solution()
    z = so.lengthOfLongestSubstring(s)
    print(z)
