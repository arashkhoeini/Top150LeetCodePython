# https://leetcode.com/problems/letter-combinations-of-a-phone-number/description/?envType=study-plan-v2&envId=top-interview-150

# Given a string containing digits from 2-9 inclusive, return all possible letter combinations that the number could represent. Return the answer in any order.

# A mapping of digits to letters (just like on the telephone buttons) is given below. Note that 1 does not map to any letters.

from typing import List

class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        dtol = {'2': ['a', 'b', 'c'],
                '3': ['d', 'e', 'f'],
                '4': ['g', 'h', 'i'],
                '5': ['j', 'k', 'l'],
                '6': ['m', 'n', 'o'],
                '7': ['p', 'q', 'r', 's'],
                '8': ['t', 'u', 'v'], 
                '9': ['w', 'x', 'y', 'z']}
        
        combs = []
        for d in digits:
            new_combs = []
            letters = dtol[d]
            for c in combs:
                for l in letters:
                    new_combs.append(c+l)
            combs = new_combs
            if len(combs) == 0:
                combs.extend(letters)
        
        return combs