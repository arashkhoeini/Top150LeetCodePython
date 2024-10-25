import unittest
from Top150 import JumpGame2, ProductExceptSelf, GasStation, Candy, MinSumSubarraySize, LongestSubstringWithoutRepeat

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
