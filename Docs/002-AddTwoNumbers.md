# [两数相加](https://leetcode-cn.com/problems/add-two-numbers/)

## 题目

> 	给你两个 非空 的链表，表示两个非负的整数。它们每位数字都是按照 逆序 的方式存储的，并且每个节点只能存储 一位 数字。
>
> 请你将两个数相加，并以相同形式返回一个表示和的链表。
>
> 你可以假设除了数字 0 之外，这两个数都不会以 0 开头。
>

## 解题思路

### 常规一

- 思路：

  ```
  输入：l1 = [2,4,3], l2 = [5,6,4]
  输出：[7,0,8]
  解释：342 + 465 = 807.
  ```

  那就按照本意进行计算

- [Python](../Python/002-AddTwoNumbers/Solution.py)

  ```java
  class Solution:
      def addTwoNumbers(self, l1: ListNode, l2: ListNode) -> ListNode:
          # 创建列表1为l1元素
          i1 = []
          while l1:
              i1.append(str(l1.val))
              l1 = l1.next
          # 创建列表2位l2元素
          i2 = []
          while l2:
              i2.append(str(l2.val))
              l2 = l2.next
          # 转换格式相加计算
          i3 = [int(i) for i in str(int(''.join(i1[::-1])) + int(''.join(i2[::-1])))]
          # 构建ListNode
          ret = None
          for i in range(len(i3)):
              if i == 0:
                  ret = ListNode(i3[i])
              else:
                  ret = ListNode(i3[i], ret)
          return ret
  ```

  - 执行用时：**84 ms**
  - 内存消耗：**15 MB**

- Java

  - 哈哈哈 扑街了 会出现容量问题，偶尔几个还是会过的，略微尴尬
  - **代码附上吧 纯属锻炼思维和代码修炼了 这是错的！ 这是错的！ 这是错的！ 这是错的！ 这是错的！**

  ```java
  class Solution {
      public ListNode addTwoNumbers(ListNode l1, ListNode l2) {
          ArrayList<Integer> i1 = new ArrayList<>();
          while (l1 != null) {
              i1.add(l1.val);
              l1 = l1.next;
          }
          ArrayList<Integer> i2 = new ArrayList<>();
          while (l2 != null) {
              i2.add(l2.val);
              l2 = l2.next;
          }
          long ret_1 = 0;
          for (int i = 0; i < i1.toArray().length; i++) {
              ret_1 += (long) (((int) i1.toArray()[i]) * (Math.pow(10, i)));
          }
  
          long ret_2 = 0;
          for (int i = 0; i < i2.toArray().length; i++) {
              ret_2 += (long) (((int) i2.toArray()[i]) * (Math.pow(10, i)));
          }
          long sum = ret_1 + ret_2;
          String ssum = String.valueOf(sum);
          int[] array_sum = new int[ssum.length()];
          for (int i = 0; i < ssum.length(); i++) {
              array_sum[i] = (int) Long.parseLong(String.valueOf(ssum.charAt(i)));
          }
          ListNode listNode = null;
          for (int i = 0; i < array_sum.length; i++) {
              if (i == 0){
                  listNode = new ListNode(array_sum[i]);
              }else{
                  listNode = new ListNode(array_sum[i], listNode);
              }
          }
          return listNode;
      }
  }
  ```

### [官方思路](https://leetcode-cn.com/problems/add-two-numbers/solution/liang-shu-xiang-jia-by-leetcode-solution/)

- 思路：大致意思就是逐位计算，有个carry表示进位。如果链表遍历结束后`carry >0`在答案链表的后面附加一个节点，节点的值为 `carry`

- 时间复杂度：![](http://latex.codecogs.com/svg.latex?O(max(m,n)))，其中 ![](http://latex.codecogs.com/svg.latex?m,n) 为两个链表的长度。我们要遍历两个链表的全部位置，而处理每个位置只需要 ![](http://latex.codecogs.com/svg.latex?O(1))的时间。

- 空间复杂度：![](http://latex.codecogs.com/svg.latex?O(max(m,n)))。答案链表的长度最多为较长链表的长度 ![](http://latex.codecogs.com/svg.latex?+1)。

- [Python](../Python/002-AddTwoNumbers/SolutionByCarry.py)

  ```python
  class Solution:
      def addTwoNumbers(self, l1: ListNode, l2: ListNode) -> ListNode:
          tmp = ret = ListNode(0)
          carry = 0
          while l1 or l2:
              sum = 0
              if l1:
                  sum = l1.val if l1 else 0
                  l1 = l1.next
              if l2:
                  sum += l2.val if l2 else 0
                  l2 = l2.next
              sum += carry
              carry = sum // 10
              ret.next = ListNode(sum % 10)
              ret = ret.next
  
              if carry:
                  ret.next = ListNode(1)
          ret = tmp.next
          return ret
  ```

  - 执行用时：**80 ms**

  - 内存消耗：**14.8 MB**

- [Java](../Java/002-AddTwoNumbers/Solution.java)

  ```java
  public class Solution {
  
      public ListNode addTwoNumbers(ListNode l1, ListNode l2) {
          int carry = 0;//进位
          ListNode sum = new ListNode(0);
          ListNode head = sum;
          while ((carry!=0 )|| l1!=null || l2!=null) {
              int val1 = l1 != null ? l1.val : 0 ;
              int val2 = l2 != null ? l2.val : 0 ;
              int r1 = val1 + val2 + carry;
              carry = r1 >= 10 ? 1 : 0;
              sum.next = new ListNode(r1 % 10);
              sum = sum.next ;
              if (l1!=null) l1 = l1.next ;
              if (l2!=null) l2 = l2.next ;
          }
          return head.next;
      }
  }
  ```

  -	执行用时：**2 ms**
  -	内存消耗：**38.6 MB**

### 万能递归

- 思路

  - 因为两个数字相加会产生进位，所以使用i来保存进位。
  - 则当前位的值为(l1.val + l2.val + i) % 10
  - 则进位值为(l1.val + l2.val + i) / 10
  - 建立新node，然后将进位传入下一层。

- [Python](../Python/002-AddTwoNumbers/SolutionByRecursion.py)

  ```python
  class Solution:
      def addTwoNumbers(self, l1: ListNode, l2: ListNode) -> ListNode:
          def addTwoNumber(l1: ListNode, l2: ListNode, carry: int) -> ListNode:
              if not l1 and not l2 and not carry: return None
              sum = (l1.val if l1 else 0) + (l2.val if l2 else 0) + carry
              node = ListNode(sum % 10)
              node.next = addTwoNumber(l1.next if l1 else None, l2.next if l2 else None, sum // 10)
              return node
          return  addTwoNumber(l1,l2,0)
  ```

  - 执行用时：**68 ms**
  - 内存消耗：**14.8 MB**

- [Java](../Java/002-AddTwoNumbers/SolutionByRecursion.java)

  ```java
  class Solution {
     public ListNode addTwoNumbers(ListNode l1, ListNode l2) {
          return addTwoNumber(l1, l2, 0);
      }
      public ListNode addTwoNumber(ListNode l1, ListNode l2 ,int carry){
          if (l1 == null && l2 == null && carry == 0) return null;
          int sum = (l1 != null ? l1.val : 0) + (l2 != null ? l2.val : 0) + carry;
          ListNode node = new ListNode(sum % 10);
          node.next = addTwoNumber(l1 != null ? l1.next : null, l2 != null ? l2.next : null, sum / 10);
          return node;
      }
  }
  ```

  - 执行用时：**2 ms**
  - 内存消耗：**38.7 MB**

### [原地修改](https://leetcode-cn.com/problems/add-two-numbers/solution/yuan-di-xiu-gai-by-xiao-sa-de-yuan-shuai-2dxo/)

- 懒得看了，有兴趣的可以看下！

  

  

  
