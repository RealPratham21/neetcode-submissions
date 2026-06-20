# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:   
    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
        def trav(node1, node2):
            if not node1:
                if not node2:
                    return True
                
                else:
                    return False
            
            if not node2:
                return True if not node1 else False
            
            res = False

            if node1.val == node2.val:
                res |= trav(node1.left, node2.left) & trav(node1.right, node2.right)
            
                # res |= trav(node1.right, node2.right)
            
            else:
                res |= trav(node1.left, subRoot)
                res |= trav(node1.right, subRoot)
            
            return res
        
        return trav(root, subRoot)