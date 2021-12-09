from functools import lru_cache
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
# class Solution:
#     def maxProduct(self, root: Optional[TreeNode]) -> int:
#         self.total = 0
#         self.total, _ = self.solver(root)
#         _, ans = self.solver(root)
#         return ans % (10**9 + 7)
        
#     def solver(self, root):
#         if not root:
#             return 0, 0
#         sum_left, max_left = self.solver(root.left)
#         sum_right, max_right = self.solver(root.right)
#         sum_bottom = sum_left + sum_right + root.val
#         ans = max(max_left, max_right, sum_left * (self.total - sum_left), sum_right * (self.total - sum_right))
#         return sum_bottom, ans

class Solution:
    def maxProduct(self, root: Optional[TreeNode]) -> int:
        self.total = self.get_sum(root)
        ans = self.solver(root)
        return ans % (10**9 + 7)

    @lru_cache(maxsize=None)
    def get_sum(self, root):
        if not root:
            return 0
        ret = self.get_sum(root.left) + self.get_sum(root.right) + root.val
        return ret
        
    @lru_cache(maxsize=None)
    def solver(self, root):
        if not root:
            return 0
        sum_left = self.get_sum(root.left)
        sum_right = self.get_sum(root.right)
        ans = max(self.solver(root.left), self.solver(root.right), sum_left * (self.total - sum_left), sum_right * (self.total - sum_right))
        return ans
