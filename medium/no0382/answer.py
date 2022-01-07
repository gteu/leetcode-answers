# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def __init__(self, head: Optional[ListNode]):
        self.head, cur = head, head
        self.len = 0
        while(cur):
            cur = cur.next
            self.len += 1
        
    def getRandom(self) -> int:
        val = random.randint(0, self.len - 1)
        cur = self.head
        for _ in range(val):
            cur = cur.next
        return cur.val

# Your Solution object will be instantiated and called as such:
# obj = Solution(head)
# param_1 = obj.getRandom()
