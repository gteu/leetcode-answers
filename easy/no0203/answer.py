# This solution doesn't make a new linked list for the answer.
# It just links necessary nodes of the original linked list, so it's relatively space-efficient.

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeElements(self, head: Optional[ListNode], val: int) -> Optional[ListNode]:
        dummy_head = ListNode(-1)
        dummy_head.next = head
        current = dummy_head
        
        while(current.next):
            if current.next.val == val:
                current.next = current.next.next
            else:
                current = current.next
        return dummy_head.next