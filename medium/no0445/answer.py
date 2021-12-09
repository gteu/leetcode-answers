# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        len1, len2 = self.getLength(l1), self.getLength(l2)
        l1, l2 = self.addLeadingZero(len2-len1, l1), self.addLeadingZero(len1-len2, l2)
        c, l = self.combineList(l1, l2)
        if c > 0:
            new = ListNode(c)
            new.next = l
            l = new
        return l

    def getLength(self, l):
        len_l = 0
        while(l):
            l = l.next
            len_l += 1
        return len_l
        
    def addLeadingZero(self, num, l):
        for i in range(num):
            new = ListNode(0)
            new.next = l
            l = new
        return l
        
    def combineList(self, l1, l2):
        if (not l1 or not l2):
            return 0, None
        
        c, new = self.combineList(l1.next, l2.next)
        s = l1.val + l2.val + c
        ret = ListNode(s % 10)
        ret.next = new
        
        return s // 10, ret
        
