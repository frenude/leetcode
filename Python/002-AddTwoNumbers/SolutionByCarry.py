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


if __name__ == '__main__':
    l1 = ListNode([9, 9, 9, 9, 9, 9, 9])
    l2 = ListNode([9, 9, 9, 9])
    s = Solution()
    ret = s.addTwoNumbers(l1, l2)
    print(ret)
