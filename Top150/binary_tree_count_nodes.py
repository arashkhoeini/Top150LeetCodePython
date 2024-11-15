# https://leetcode.com/problems/count-complete-tree-nodes/description/?envType=study-plan-v2&envId=top-interview-150

# Given the root of a complete binary tree, return the number of the nodes in the tree.

# According to Wikipedia, every level, except possibly the last, is completely filled in a complete binary tree, and all nodes in the last level are as far left as possible. It can have between 1 and 2h nodes inclusive at the last level h.

# Design an algorithm that runs in less than O(n) time complexity.

from typing import Optional
from .binary_tree_max_depth import TreeNode
class Solution:
    def countNodes(self, root: Optional[TreeNode]) -> int:
        
        if root == None: return 0

        # pre-order
        self.n_nodes = 0
        def preorder(node):
            self.n_nodes += 1
            if node.left: preorder(node.left)
            if node.right: preorder(node.right)
            
        
        preorder(root)
        return self.n_nodes