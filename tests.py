import unittest
from Top150 import JumpGame2, ProductExceptSelf, GasStation, Candy, MinSumSubarraySize, LongestSubstringWithoutRepeat, ValidSudoku, RotateImage
from Top150 import GameOfLife

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