# https://leetcode.com/problems/invert-binary-tree/?envType=study-plan-v2&envId=top-interview-150

# Given the root of a binary tree, invert the tree, and return its root.


from typing import Optional
from .binary_tree_max_depth import TreeNode

class Solution:
    def invertTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        nodes = [root]
        if root is None: return None
        while len(nodes)>0:
            node = nodes.pop(0)
            if node.left: nodes.append(node.left)
            if node.right: nodes.append(node.right)
            node.left, node.right = node.right, node.left
        
        return root