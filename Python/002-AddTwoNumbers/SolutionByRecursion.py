# !/usr/bin/env Python3
# -*- coding: utf-8 -*-

#  @Author: Frenude 
#  @Description:
#  @Date: Created in 01 05,2021
#  @Modified By:

class ListNode():
    def __init__(self, val, next=None):
        if isinstance(val, int):
            self.val = val
            self.next = next

        elif isinstance(val, list):
            self.val = val[0]
            self.next = next
            cur = self
            for i in val[1:]:
                cur.next = ListNode(i)
                cur = cur.next

    def gatherAttrs(self):
        return ", ".join("{}: {}".format(k, getattr(self, k)) for k in self.__dict__.keys())

    def __str__(self):
        return self.__class__.__name__ + " {" + "{}".format(self.gatherAttrs()) + "}"


class Solution:
    def addTwoNumbers(self, l1: ListNode, l2: ListNode) -> ListNode:
        def addTwoNumber(l1: ListNode, l2: ListNode, carry: int) -> ListNode:
            if not l1 and not l2 and not carry: return None
            sum = (l1.val if l1 else 0) + (l2.val if l2 else 0) + carry
            node = ListNode(sum % 10)
            node.next = addTwoNumber(l1.next if l1 else None, l2.next if l2 else None, sum // 10)
            return node
        return  addTwoNumber(l1,l2,0)


if __name__ == '__main__':
    l1 = ListNode([9, 9, 9, 9, 9, 9, 9])
    l2 = ListNode([9, 9, 9, 9])
    s = Solution()
    ret = s.addTwoNumbers(l1, l2)
    print(ret)
