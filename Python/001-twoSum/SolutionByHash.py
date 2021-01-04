# !/usr/bin/env Python3
# -*- coding: utf-8 -*-

#  @Author: Frenude 
#  @Description:
#  @Date: Created in 01 04,2021
#  @Modified By:
from typing import List


class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        hash = {}
        for i, v in enumerate(nums):
            # 可以使用 if hash.get(target - v) is not None: 实测 in 比 get 快一点
            if (target - v) in hash:
                return [hash.get(target - v), i]
            hash[v] = i


if __name__ == '__main__':
    nums = [2, 7, 11, 15]
    target = 9
    s = Solution()
    print(s.twoSum(nums, target))
