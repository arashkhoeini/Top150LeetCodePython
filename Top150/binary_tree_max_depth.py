# https://leetcode.com/problems/maximum-depth-of-binary-tree/solutions/?envType=study-plan-v2&envId=top-interview-150

# A binary tree's maximum depth is the number of nodes along the longest path from the root node down to the farthest leaf node.


from typing import Optional

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        
        def recursive(root, depth):
            if root is None:
                return depth
            else: 
                return max(recursive(root.left, depth+1), recursive(root.right, depth+1))
        
        if root is None: return 0
        max_depth = recursive(root, 0)
        return max_depth
    