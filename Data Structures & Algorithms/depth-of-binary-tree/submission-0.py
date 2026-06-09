# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        
        def get_depth(node):
            if not node:
                return 0
            
            left = get_depth(node.left) + 1
            right = get_depth(node.right) + 1

            return max(left, right)
        
        return get_depth(root)