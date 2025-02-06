# https://leetcode.com/problems/binary-tree-level-order-traversal/description/?envType=study-plan-v2&envId=top-interview-150

# Given the root of a binary tree, return the level order traversal of its nodes' values. (i.e., from left to right, level by level).


from typing import List, Optional
from Top150.binary_tree_max_depth import TreeNode

class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        
        if root is None:
            return []

        current_level = 1
        q = [(current_level, root)]
        output = [[]]
        while q:
            level, node = q.pop(0)
            if level == current_level:
                output[-1].append(node.val)
            elif level == current_level + 1:
                output.append([node.val])
                current_level += 1

            if node.left: q.append((level+1, node.left))
            if node.right: q.append((level+1, node.right))

        return output