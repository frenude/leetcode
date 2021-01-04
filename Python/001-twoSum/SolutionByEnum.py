# !/usr/bin/env Python3
# -*- coding: utf-8 -*-

#  @Author: Frenude 
#  @Description:
#  @Date: Created in 01 04,2021
#  @Modified By:
from typing import List


class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        for i in range(len(nums)):
            for j in range(i + 1, len(nums)):
                if nums[i] + nums[j] == target:
                    return [i, j]


if __name__ == '__main__':
    nums = [2, 7, 11, 15]
    target = 9
    s = Solution()
    print(s.twoSum(nums, target))
