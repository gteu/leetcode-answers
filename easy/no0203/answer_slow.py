# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeElements(self, head: Optional[ListNode], val: int) -> Optional[ListNode]:
        if head is None:
            return None
        ret = ListNode(0)
        ret_head = ret
        while(head):
            if head.val != val:
                ret.next = ListNode(head.val)
                ret = ret.next
            head = head.next
        return ret_head.next
