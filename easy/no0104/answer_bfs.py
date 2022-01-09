# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        same_depth_nodes = [root] if root else None 
        depth = 0
        while same_depth_nodes:
            depth += 1
            next_depth_nodes = []
            for node in same_depth_nodes:
                if node.left:
                    next_depth_nodes.append(node.left) 
                if node.right:
                    next_depth_nodes.append(node.right)
            same_depth_nodes = next_depth_nodes
        return depth