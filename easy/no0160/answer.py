# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

# class Solution:
#     def getIntersectionNode(self, headA: ListNode, headB: ListNode) -> ListNode:
#         A, B = headA, headB
#         while A != B:
#             A = A.next if A else headB
#             B = B.next if B else headA
#         return A

class Solution:
    def getIntersectionNode(self, headA: ListNode, headB: ListNode) -> ListNode:
        lenA, lenB = self.getLength(headA), self.getLength(headB)
        A, B = self.addLeadingZero(lenB - lenA, headA), self.addLeadingZero(lenA - lenB, headB)
        while(A != B):
            A = A.next
            B = B.next
        return A
        
    def addLeadingZero(self, num, head):
        for _ in range(num):
            new = ListNode(0)
            new.next = head
            head = new
        return head
        
    def getLength(self, head):
        ret = 0
        while(head):
            head = head.next
            ret += 1
        return ret
