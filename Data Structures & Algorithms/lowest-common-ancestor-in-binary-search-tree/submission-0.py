# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def lowestCommonAncestor(self, root: TreeNode, p: TreeNode, q: TreeNode) -> TreeNode:
        c_to_p = {}

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

        def backtrack(node_p, node_q):
            if node_p.val == node_q.val:
                return node_p
            
            final_res = None

            if node_q.val in c_to_p and node_p in c_to_p:
                res = backtrack(c_to_p[node_p.val], c_to_p[node_q.val])

                if res:
                    final_res = res

            if node_p.val in c_to_p:
                res = backtrack(c_to_p[node_p.val], node_q)

                if res:
                    final_res = res
            
            if node_q.val in c_to_p:
                res = backtrack(node_p, c_to_p[node_q.val])

                if res:
                    final_res = res
            
            return final_res
        
        return backtrack(p, q)
