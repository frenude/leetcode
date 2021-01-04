# [两数之和](https://leetcode-cn.com/problems/two-sum)

## 题目：

> 	给定一个整数数组 nums 和一个整数目标值 target，请你在该数组中找出 和为目标值 的那 两个 整数，并返回它们的数组下标。
>
> 你可以假设每种输入只会对应一个答案。但是，数组中同一个元素不能使用两遍。
>
> 你可以按任意顺序返回答案。
>

## 解题思路：

### 暴力枚举

- 思路：

  - 循环遍历数组，找到 `num`和`target-num`
  
- 时间复杂度：![](http://latex.codecogs.com/svg.latex?O(N^2)),其中 N是数组中的元素数量。最坏情况下数组中任意两个数都要被匹配一次。

- 空间复杂度：![](http://latex.codecogs.com/svg.latex?O(1))。

- 优化思路:

  - 因为同一元素不能使用两遍，只需要在 `num` 后面的元素中寻找 `target - num`。

- Python

  ```python
  class Solution:
      def twoSum(self, nums: List[int], target: int) -> List[int]:
          # 第一次遍历找到 nums 中的 num
          for i in range(len(nums)):
              # 在nums[num:] 中寻找target-num
              for j in range(i + 1, len(nums)):
                  if nums[i] + nums[j] == target:
                      return [i, j]
  ```

  - 执行用时：**36 ms**
  - 内存消耗：**14.8 MB**

- Java

  ```java
  class Solution {
      public int[] twoSum(int[] nums, int target) {
          // 第一次遍历找到 nums 中的 num
          for (int i = 0; i < nums.length; i++) {
              // 在nums[num:] 中寻找target-num
              for (int j = i + 1; j < nums.length; j++) {
                  if ((nums[i] + nums[j]) == target) {
                      return new int[]{i, j};
                  }
              }
          }
          return new int[0];
      }
  }
  ```
  
  - 执行用时: **0 ms**
  - 内存消耗: **38.5 MB**

### 哈希表

- 思路：

  - 因为查询`target-num`时间复杂度过高，考虑采用`HashMap`降低时间复杂度
  - 构建`HashMap(值,索引)`通过判断`target-num`是否在`hashMap`中,然后将 `num` 插入到哈希表中，即可保证不会让 `num` 和自己匹配
  - 时间复杂度：![](http://latex.codecogs.com/svg.latex?O(N))，其中 N 是数组中的元素数量。对于每一个元素 `num`，我们可以 ![](http://latex.codecogs.com/svg.latex?O(1))地寻找 `target - num`。
  - 空间复杂度：![](http://latex.codecogs.com/svg.latex?O(N))，其中 N是数组中的元素数量。主要为哈希表的开销。

- Python

  ```python
  class Solution:
      def twoSum(self, nums: List[int], target: int) -> List[int]:
          hash = {}
          for i, v in enumerate(nums):
              # 可以使用 if hash.get(target - v) is not None: 实测 in 比 get 快一点
              if (target - v) in hash:
                  return [hash.get(target - v), i]
              hash[v] = i
  ```

  - 执行用时：**36 ms**
  - 内存消耗：**14.8 MB**

- Java

  ```java
  class Solution {
      public int[] twoSum(int[] nums, int target) {
          HashMap<Integer, Integer> hashMap = new HashMap<>();
          for (int i = 0; i < nums.length; i++) {
              if (hashMap.containsKey(target - nums[i])) {
                  return new int[]{hashMap.get(target - nums[i]), i};
              }
              hashMap.put(nums[i], i);
          }
          return new int[0];
      }
  }
  ```

  - 执行用时：**0 ms**
  - 内存消耗：**38.5 MB**

  

  
