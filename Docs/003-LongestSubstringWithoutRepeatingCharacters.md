# [无重复字符的最长子串](https://leetcode-cn.com/problems/longest-substring-without-repeating-characters/)

## 题目：

> ​	给定一个字符串，请你找出其中不含有重复字符的 **最长子串** 的长度。
>
> ```
> 输入: s = "abcabcbb"
> 输出: 3 
> 解释: 因为无重复字符的最长子串是 "abc"，所以其长度为 3。
> ```

## 解题思路：

### 暴力破解

- 思路：
  1. 循环遍历
  2. 用一个容器装不重复的元素，如果遇到重复数据说明重复。停止循环，
  3. 找出当次循环最大不重复字符串，
  4. 多次循环找出字符串中不重复的最长长度
  
- 时间复杂度:![](http://latex.codecogs.com/svg.latex?O(N^2))

- Python

  ```python
  class Solution:
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
  ```

  - 执行用时: **520 ms**
  - 内存消耗: **14.9 MB**

- Java

  ```java
  public class Solution {
      public int lengthOfLongestSubstring(String s) {
          if (s == null && s.length() == 0) {
              return 0;
          }
          int max_l = 0;
          HashSet<Character> set = new HashSet<>();
          for (int i = 0; i < s.length(); i++) {
              int l = 0;
              for (int j = i; j < s.length(); j++) {
                  if (set.contains(s.charAt(j))) {
                      break;
                  }
                  set.add(s.charAt(j));
                  l++;
              }
              max_l = Math.max(l, max_l);
              set.clear();
          }
          return max_l;
      }
  }
  ```

  - 执行用时: **97 ms**
  - 内存消耗: **39 MB**

### [滑动窗口](https://leetcode-cn.com/problems/longest-substring-without-repeating-characters/solution/wu-zhong-fu-zi-fu-de-zui-chang-zi-chuan-by-leetc-2/)

- 思路：

  - 所谓的滑动窗口就是指双指针

  ![滑动窗口](https://pic.leetcode-cn.com/8b7cac826e572c65f8b77e0f380eaa93ab665857a8e916bc4ea36b7765eafc55-%E5%9B%BE%E7%89%87.png)
  
- 时间复杂度：![](http://latex.codecogs.com/svg.latex?O(N))，其中![](http://latex.codecogs.com/svg.latex?N) 是字符串的长度。左指针和右指针分别会遍历整个字符串一次。

- 空间复杂度：![](http://latex.codecogs.com/svg.latex?O(|\Sigma|))，其中 ![](http://latex.codecogs.com/svg.latex?\Sigma) 表示字符集（即字符串中可以出现的字符），![](http://latex.codecogs.com/svg.latex?|\Sigma|) 表示字符集的大小。

- Python

  ```python
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
  ```

  - 执行用时: **80 ms**
  - 内存消耗: **15 MB**

- Java

  ```java
  public class Solution {
      public int lengthOfLongestSubstring(String s) {
          int l = -1;
          int r = 0;
          HashMap<Character, Integer> map = new HashMap<>();
          for (int i = 0; i < s.length(); i++) {
              if (map.containsKey(s.charAt(i)) && map.get(s.charAt(i)) > l) {
                  l = map.get(s.charAt(i));
                  map.put(s.charAt(i), i);
              } else {
                  map.put(s.charAt(i), i);
                  r = Math.max(r, i - l);
              }
          }
          return r;
      }
  }
  ```

  - 执行用时: **7 ms**
  - 内存消耗: **38.6 MB**

  

  