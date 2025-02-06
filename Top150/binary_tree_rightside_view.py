# https://leetcode.com/problems/binary-tree-right-side-view/description/?envType=study-plan-v2&envId=top-interview-150

# Given the root of a binary tree, imagine yourself standing on the right side of it, return the values of the nodes you can see ordered from top to bottom.

from typing import List, Optional
from Top150.binary_tree_max_depth import TreeNode

class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        
        if root is None:
            return []
        stack = [(1, root)]
        view = []
        current_level = 1
        while stack:
            level, node = stack.pop()
            if level == current_level: 
                view.append(node.val)
                current_level += 1
            if node.left: stack.append((level+1, node.left))
            if node.right: stack.append((level+1, node.right))

        return view