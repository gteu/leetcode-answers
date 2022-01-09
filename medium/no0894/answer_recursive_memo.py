# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    memo = {}
    def allPossibleFBT(self, n: int) -> List[Optional[TreeNode]]:
        orig_n = n
        if orig_n in self.memo.keys():
            return self.memo[orig_n]
        n -= 1
        if n == 0: return [TreeNode(0)]
        ret = []
        for i in range(1, n, 2):
            for left in self.allPossibleFBT(i):
                for right in self.allPossibleFBT(n-i):
                    root = TreeNode(0)
                    root.left = left
                    root.right = right
                    ret.append(root)
        self.memo[orig_n] = ret
        return ret