# https://leetcode.com/problems/coin-change/?envType=study-plan-v2&envId=top-interview-150

# You are given an integer array coins representing coins of different denominations and an integer amount representing a total amount of money.

# Return the fewest number of coins that you need to make up that amount. If that amount of money cannot be made up by any combination of the coins, return -1.

# You may assume that you have an infinite number of each kind of coin.

from typing import List

class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        if amount == 0: return 0
        def dp(a):
            # print(memo)
            if a == 0: return True
            if a in memo: return memo[a]
            if a in coins: 
                memo[a] = 1
                return memo[a]

            for c in coins:
                if a >= c:
                    memo[a] = min(1+dp(a-c), memo.get(a, float('inf')))
            
            return memo.get(a, float('inf'))
        memo = {}
        dp(amount)
        print(memo)
        result = memo.get(amount, -1)
        print(result)
        if result == float('inf'): 
            return -1
        else:
            return result