# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def allPossibleFBT(self, n: int) -> List[Optional[TreeNode]]:
        n -= 1
        if n == 0: return [TreeNode(0)]
        ret = []
        for i in range(1, n, 2):
            for left in self.allPossibleFBT(i):
                for right in self.allPossibleFBT(n-i):
                    root = TreeNode(0)
                    root.left = left
                    root.right = right
                    ret += [root]
        return ret
