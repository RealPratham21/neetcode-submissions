"""
# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []
"""

class Solution:
    def cloneGraph(self, node: Optional['Node']) -> Optional['Node']:

        node_map = {}

        def dfs(orig):
            if not orig:
                return None

            new_node = Node(orig.val)

            node_map[orig.val] = new_node

            for i in orig.neighbors:

                if i.val in node_map:
                    new_node.neighbors.append(node_map[i.val])
                else:
                    new_node.neighbors.append(dfs(i))

            return new_node
        
        return dfs(node)