# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        ans = True

        def find(node):
            nonlocal ans
            if node.left:
                if node.left.val < node.val:
                    find(node.left)
                
                else:
                    ans = False
            
            if node.right:
                if node.right.val > node.val:
                    find(node.right)
                
                else:
                    ans = False
        
        find(root)

        return ans