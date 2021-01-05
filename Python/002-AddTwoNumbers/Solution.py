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
        i1 = []
        while l1:
            i1.append(str(l1.val))
            l1 = l1.next
        i2 = []
        while l2:
            i2.append(str(l2.val))
            l2 = l2.next
        i3 = [int(i) for i in str(int(''.join(i1[::-1])) + int(''.join(i2[::-1])))]
        ret = None
        for i in range(len(i3)):
            if i == 0:
                ret = ListNode(i3[i])
            else:
                ret = ListNode(i3[i], ret)
        return ret


if __name__ == '__main__':
    l1 = ListNode([2, 4, 3])
    l2 = ListNode([5, 6, 4])
    s = Solution()
    ret = s.addTwoNumbers(l1, l2)
    print(ret)
