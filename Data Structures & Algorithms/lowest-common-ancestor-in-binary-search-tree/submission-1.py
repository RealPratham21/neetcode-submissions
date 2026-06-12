# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def lowestCommonAncestor(self, root: TreeNode, p: TreeNode, q: TreeNode) -> TreeNode:
        c_to_p = {}
        c_to_p[root.val] = None

        def construct(node):
            if not node:
                return

            if node.left:
                c_to_p[node.left.val] = node
                construct(node.left)
            
            if node.right:
                c_to_p[node.right.val] = node
                construct(node.right)
        
        construct(root)

        curr = p
        seen = set()

        while curr:
            if curr.val in seen:
                break
            
            seen.add(curr.val)

            curr = c_to_p[curr.val]
        
        curr = q

        while curr:
            if curr.val in seen:
                return curr
            
            seen.add(curr.val)

            curr = c_to_p[curr.val]
        
        return None