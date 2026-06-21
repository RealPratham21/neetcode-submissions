# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:   
    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
        def solve(node1, node2):
            if not node1 or not node2:
                return False

            if not node2.left and not node2.right:
                return not node1.left and not node1.right
            
            res = False

            if node1.val == node2.val:
                res |= solve(node1.left, node2.left) & solve(node1.right, node2.right)
            
            else:
                res |= solve(node1.left, subRoot)
                res |= solve(node1.right, subRoot)
            
            return res
        
        return solve(root, subRoot)