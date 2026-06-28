# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        
        def find(node, lower, upper):
            if node is None:
                return True
            
            if not (lower < node.val < upper):
                return False
            
            return find(node.left, lower, node.val) and find(node.right, node.val, upper)
        
        return find(root, float('-inf'), float('inf'))