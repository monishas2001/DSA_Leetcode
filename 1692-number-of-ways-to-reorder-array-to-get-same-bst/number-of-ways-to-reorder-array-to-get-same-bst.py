from math import comb

class Solution:
    def numOfWays(self, nums):
        MOD = 10**9 + 7

        def solve(nums):
            if len(nums) < 3:
                return 1

            root = nums[0]
            left = [x for x in nums[1:] if x < root]
            right = [x for x in nums[1:] if x > root]

            ways = comb(len(nums) - 1, len(left))
            return ways * solve(left) * solve(right) % MOD

        return (solve(nums) - 1) % MOD