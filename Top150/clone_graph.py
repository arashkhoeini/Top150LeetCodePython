# https://leetcode.com/problems/clone-graph/description/?envType=study-plan-v2&envId=top-interview-150

# Given a reference of a node in a connected undirected graph.

# Return a deep copy (clone) of the graph.

# Each node in the graph contains a value (int) and a list (List[Node]) of its neighbors.

from typing import Optional


class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []

class Solution:
    def cloneGraph(self, node: Optional['Node']) -> Optional['Node']:
        
        if node is None: return None

        visited = set([node])
        q = [node]
        new_node = Node(val=node.val)
        node_dict = {node.val:new_node}
        while q:
            n = q.pop(0)
            for nei in n.neighbors:
                if nei not in visited:
                    nn = Node(val=nei.val, neighbors=[node_dict[n.val]])
                    node_dict[n.val].neighbors.append(nn)
                    node_dict[nn.val] = nn
                    q.append(nei)
                    visited.add(nei)
                else:
                    if node_dict[n.val] not in node_dict[nei.val].neighbors:
                        node_dict[nei.val].neighbors.append(node_dict[n.val])
                        node_dict[n.val].neighbors.append(node_dict[nei.val])
        
        return new_node