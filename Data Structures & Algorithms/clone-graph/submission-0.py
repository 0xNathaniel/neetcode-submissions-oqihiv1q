"""
# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []
"""

class Solution:
    def cloneGraph(self, node: Optional['Node']) -> Optional['Node']:
        if not node:
            return None

        newNodes = {}
        newNodes[node] = Node(node.val)
        q = deque([node])

        while q:
            cur = q.pop()

            for n in cur.neighbors:
                if n not in newNodes:
                    newNodes[n] = Node(n.val)
                    q.append(n)
                newNodes[cur].neighbors.append(newNodes[n])

        return newNodes[node]
