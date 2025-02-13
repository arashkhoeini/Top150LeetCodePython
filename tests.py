import unittest
from Top150 import JumpGame2, ProductExceptSelf, GasStation, Candy, MinSumSubarraySize, LongestSubstringWithoutRepeat, ValidSudoku, RotateImage
from Top150 import GameOfLife, RansomNote, ValidAnagram, GroupAnagrams, NearbyDuplicates, BinaryTreeMaxDepth, BinaryTreeInvert
from Top150 import BinaryTreeConstructionPreorderInorder, BinaryTreeConstructionPostorderInorder, BinaryTreeFlatten, CountBinaryTreeNodes
from Top150 import BSTMinimumAbsoluteDifference, BSTKthSmallestElement, BSTValidTree, SimplifyPath, BinaryTreeRightSideView
from Top150 import BinaryTreeLevelOrderTraversal, NumberOfIslands, ConvertSortedArrayToBinarySearchTree, SnakesAndLadders

from Top150.binary_tree_max_depth import TreeNode
class TestSolutions(unittest.TestCase):

    def test_jump_game_2(self):
        self.assertEqual(JumpGame2().jump([2,3,1,1,4]), 2)
        self.assertEqual(JumpGame2().jump([2,3,0,1,4]), 2)
    
    def test_product_of_array_except_self(self):
        self.assertEqual(ProductExceptSelf().productExceptSelf([1,2,3,4]), [24,12,8,6])
        self.assertEqual(ProductExceptSelf().productExceptSelf([-1,1,0,-3,3]), [0,0,9,0,0])

    def test_gas_station(self):
        self.assertEqual(GasStation().canCompleteCircuit([1,2,3,4,5], [3,4,5,1,2]), 3)
        self.assertEqual(GasStation().canCompleteCircuit([2,3,4], [3,4,3]), -1)

    def test_candy(self):
        self.assertEqual(Candy().candy([1,0,2]), 5) 
        self.assertEqual(Candy().candy([1,2,2]), 4)
    
    def test_min_sum_subarray_size(self):
        self.assertEqual(MinSumSubarraySize().minSubArrayLen(7, [2,3,1,2,4,3]), 2)
        self.assertEqual(MinSumSubarraySize().minSubArrayLen(4, [1,4,4]), 1)
        self.assertEqual(MinSumSubarraySize().minSubArrayLen(11, [1,1,1,1,1,1,1,1]), 0)
    
    def test_longest_substring_without_repeating_characters(self):
        self.assertEqual(LongestSubstringWithoutRepeat().lengthOfLongestSubstring("abcabcbb"), 3)
        self.assertEqual(LongestSubstringWithoutRepeat().lengthOfLongestSubstring("bbbbb"), 1)
        self.assertEqual(LongestSubstringWithoutRepeat().lengthOfLongestSubstring("pwwkew"), 3)
    
    def test_valid_sudoku(self):
        board = [["5","3",".",".","7",".",".",".","."],["6",".",".","1","9","5",".",".","."],[".","9","8",".",".",".",".","6","."],["8",".",".",".","6",".",".",".","3"],["4",".",".","8",".","3",".",".","1"],["7",".",".",".","2",".",".",".","6"],[".","6",".",".",".",".","2","8","."],[".",".",".","4","1","9",".",".","5"],[".",".",".",".","8",".",".","7","9"]]
        self.assertEqual(ValidSudoku().isValidSudoku(board), True)
        board = [["8","3",".",".","7",".",".",".","."],["6",".",".","1","9","5",".",".","."],[".","9","8",".",".",".",".","6","."],["8",".",".",".","6",".",".",".","3"],["4",".",".","8",".","3",".",".","1"],["7",".",".",".","2",".",".",".","6"],[".","6",".",".",".",".","2","8","."],[".",".",".","4","1","9",".",".","5"],[".",".",".",".","8",".",".","7","9"]]
        self.assertEqual(ValidSudoku().isValidSudoku(board), False)

    def test_rotate_image(self):
        image = [[1,2,3],[4,5,6],[7,8,9]]
        solution = [[7,4,1],[8,5,2],[9,6,3]]
        RotateImage().rotate(image)
        self.assertEqual(image, solution)
        image = [[5,1,9,11],[2,4,8,10],[13,3,6,7],[15,14,12,16]]
        solution = [[15,13,2,5],[14,3,4,1],[12,6,8,9],[16,7,10,11]]
        RotateImage().rotate(image)
        self.assertEqual(image, solution)

    def test_game_of_life(self):
        board = [[0,1,0],[0,0,1],[1,1,1],[0,0,0]]
        solution = [[0,0,0],[1,0,1],[0,1,1],[0,1,0]]
        GameOfLife().gameOfLife(board)
        self.assertEqual(board, solution)
        board = [[1,1],[1,0]]
        solution = [[1,1],[1,1]]
        GameOfLife().gameOfLife(board)
        self.assertEqual(board, solution)
    
    def test_ransom_note(self):
        self.assertEqual(RansomNote().canConstruct('a', 'b'), False)
        self.assertEqual(RansomNote().canConstruct('aa', 'ab'), False)
        self.assertEqual(RansomNote().canConstruct('aa', 'aab'), True)
    
    def test_valid_anagram(self):
        self.assertTrue(ValidAnagram().isAnagram('anagram', 'nagaram'))
        self.assertFalse(ValidAnagram().isAnagram('rat', 'car'))
    
    def test_group_anagrams(self):
        self.assertEqual(GroupAnagrams().groupAnagrams(["eat","tea","tan","ate","nat","bat"]), [["eat","tea","ate"],["tan","nat"],["bat"]])
        self.assertEqual(GroupAnagrams().groupAnagrams([""]), [[""]])
        self.assertEqual(GroupAnagrams().groupAnagrams(["a"]), [["a"]])
    
    def test_nearby_duplicates(self):
        self.assertTrue(NearbyDuplicates().containsNearbyDuplicate([1,2,3,1], 3))
        self.assertTrue(NearbyDuplicates().containsNearbyDuplicate([1,0,1,1], 1))
        self.assertFalse(NearbyDuplicates().containsNearbyDuplicate([1,2,3,1,2,3], 2))

    def test_binary_tree_max_depth(self):
        
        root = TreeNode(3)
        root.left = TreeNode(9)
        root.right = TreeNode(20)
        root.right.left = TreeNode(15)
        root.right.right = TreeNode(7)
        self.assertEqual(BinaryTreeMaxDepth().maxDepth(root), 3)
        self.assertEqual(BinaryTreeMaxDepth().maxDepth(None), 0)
    
    def test_binary_tree_invert(self):
        root = TreeNode(4)
        root.left = TreeNode(2)
        root.right = TreeNode(7)
        root.left.left = TreeNode(1)
        root.left.right = TreeNode(3)
        root.right.left = TreeNode(6)
        root.right.right = TreeNode(9)
        BinaryTreeInvert().invertTree(root)
        self.assertEqual(root.val, 4)
        self.assertEqual(root.left.val, 7)
        self.assertEqual(root.right.val, 2)
        self.assertEqual(root.left.left.val, 9)
        self.assertEqual(root.left.right.val, 6)
        self.assertEqual(root.right.left.val, 3)
        self.assertEqual(root.right.right.val, 1)

    def test_binary_tree_construction_preorder_inorder(self):
        preorder = [3,9,20,15,7]
        inorder = [9,3,15,20,7]
        root = BinaryTreeConstructionPreorderInorder().buildTree(preorder, inorder)
        self.assertEqual(root.val, 3)
        self.assertEqual(root.left.val, 9)
        self.assertEqual(root.right.val, 20)
        self.assertEqual(root.right.left.val, 15)
        self.assertEqual(root.right.right.val, 7)

    def test_binary_tree_construction_postorder_inorder(self):
        postorder = [9,15,7,20,3]
        inorder = [9,3,15,20,7]
        root = BinaryTreeConstructionPostorderInorder().buildTree(inorder, postorder)
        self.assertEqual(root.val, 3)
        self.assertEqual(root.left.val, 9)
        self.assertEqual(root.right.val, 20)
        self.assertEqual(root.right.left.val, 15)
        self.assertEqual(root.right.right.val, 7)

    def test_binary_tree_flatten(self):
        root = TreeNode(1)
        root.left = TreeNode(2)
        root.right = TreeNode(5)
        root.left.left = TreeNode(3)
        root.left.right = TreeNode(4)
        root.right.right = TreeNode(6)
        BinaryTreeFlatten().flatten(root)
        self.assertEqual(root.val, 1)
        self.assertEqual(root.right.val, 2)
        self.assertEqual(root.right.right.val, 3)
        self.assertEqual(root.right.right.right.val, 4)
        self.assertEqual(root.right.right.right.right.val, 5)
        self.assertEqual(root.right.right.right.right.right.val, 6)

    def test_binary_tree_count_nodes(self):
        root = TreeNode(1)
        root.left = TreeNode(2)
        root.right = TreeNode(5)
        root.left.left = TreeNode(3)
        root.left.right = TreeNode(4)
        root.right.right = TreeNode(6)
        self.assertEqual(CountBinaryTreeNodes().countNodes(root), 6)

    def test_bst_minimum_absolute_difference(self):
        root = TreeNode(4)
        root.left = TreeNode(2)
        root.right = TreeNode(6)
        root.left.left = TreeNode(1)
        root.left.right = TreeNode(3)
        self.assertEqual(BSTMinimumAbsoluteDifference().getMinimumDifference(root), 1)
        root = TreeNode(1)
        root.right = TreeNode(3)
        root.right.left = TreeNode(2)
        self.assertEqual(BSTMinimumAbsoluteDifference().getMinimumDifference(root), 1)

    def test_bst_kth_smallest_element(self):
        root = TreeNode(3)
        root.left = TreeNode(1)
        root.right = TreeNode(4)
        root.left.right = TreeNode(2)
        self.assertEqual(BSTKthSmallestElement().kthSmallest(root, 1), 1)
        self.assertEqual(BSTKthSmallestElement().kthSmallest(root, 2), 2)
        self.assertEqual(BSTKthSmallestElement().kthSmallest(root, 3), 3)
        self.assertEqual(BSTKthSmallestElement().kthSmallest(root, 4), 4)

    def test_bst_valid_tree(self):
        root = TreeNode(2)
        root.left = TreeNode(1)
        root.right = TreeNode(3)
        self.assertTrue(BSTValidTree().isValidBST(root))
        root = TreeNode(5)
        root.left = TreeNode(1)
        root.right = TreeNode(4)
        root.right.left = TreeNode(3)
        root.right.right = TreeNode(6)
        self.assertFalse(BSTValidTree().isValidBST(root))
        root = TreeNode(5)
        root.left = TreeNode(4)
        root.right = TreeNode(6)
        root.right.left = TreeNode(3)
        root.right.right = TreeNode(7)
        self.assertFalse(BSTValidTree().isValidBST(root))

    def test_simplify_path(self):
        self.assertEqual(SimplifyPath().simplifyPath("/home/"), "/home")
        self.assertEqual(SimplifyPath().simplifyPath("/home//foo/"), "/home/foo")
        self.assertEqual(SimplifyPath().simplifyPath("/home/user/Documents/../Pictures"), "/home/user/Pictures")
        self.assertEqual(SimplifyPath().simplifyPath("/../"), "/")
        self.assertEqual(SimplifyPath().simplifyPath("/.../a/../b/c/../d/./"), "/.../b/d")

    def test_binary_tree_right_side_view(self):
        root = TreeNode(1)
        root.left = TreeNode(2)
        root.right = TreeNode(3)
        root.left.right = TreeNode(5)
        root.right.right = TreeNode(4)
        self.assertEqual(BinaryTreeRightSideView().rightSideView(root), [1,3,4])
        root = TreeNode(1)
        root.right = TreeNode(3)
        self.assertEqual(BinaryTreeRightSideView().rightSideView(root), [1,3])
        root = TreeNode(1)
        root.left = TreeNode(2)
        root.left.left = TreeNode(4)
        root.right = TreeNode(3)
        root.right.right = TreeNode(5)
        self.assertEqual(BinaryTreeRightSideView().rightSideView(root), [1,3,5])

    def test_binary_tree_level_order_traversal(self):
        root = TreeNode(3)
        root.left = TreeNode(9)
        root.right = TreeNode(20)
        root.right.left = TreeNode(15)
        root.right.right = TreeNode(7)
        self.assertEqual(BinaryTreeLevelOrderTraversal().levelOrder(root), [[3],[9,20],[15,7]])
        root = TreeNode(1)
        root.left = TreeNode(2)
        root.right = TreeNode(3)
        root.left.left = TreeNode(4)
        root.left.right = TreeNode(5)
        root.right.left = TreeNode(6)
        root.right.right = TreeNode(7)
        self.assertEqual(BinaryTreeLevelOrderTraversal().levelOrder(root), [[1],[2,3],[4,5,6,7]])

        def test_number_of_islands(self):
            grid = [["1","1","1","1","0"],["1","1","0","1","0"],["1","1","0","0","0"],["0","0","0","0","0"]]
            self.assertEqual(NumberOfIslands().numIslands(grid), 1)
            grid = [["1","1","0","0","0"],["1","1","0","0","0"],["0","0","1","0","0"],["0","0","0","1","1"]]
            self.assertEqual(NumberOfIslands().numIslands(grid), 3)

    def test_convert_sorted_array_to_binary_search_tree(self):
        nums = [-10,-3,0,5,9]
        root = ConvertSortedArrayToBinarySearchTree().sortedArrayToBST(nums)
        self.assertEqual(root.val, 0)
        self.assertEqual(root.left.val, -3)
        self.assertEqual(root.left.left.val, -10)
        self.assertEqual(root.right.val, 9)
        self.assertEqual(root.right.left.val, 5)

    def test_snakes_and_ladders(self):
        board = [[-1,-1,-1,-1,-1,-1],
                 [-1,-1,-1,-1,-1,-1],
                 [-1,-1,-1,-1,-1,-1],
                 [-1,35,-1,-1,13,-1],
                 [-1,-1,-1,-1,-1,-1],
                 [-1,15,-1,-1,-1,-1]]
        self.assertEqual(SnakesAndLadders().snakesAndLadders(board), 4)
        board = [[-1,-1,-1],
                 [-1,9,8],
                 [-1,8,9]]
        self.assertEqual(SnakesAndLadders().snakesAndLadders(board), 1)
        
        