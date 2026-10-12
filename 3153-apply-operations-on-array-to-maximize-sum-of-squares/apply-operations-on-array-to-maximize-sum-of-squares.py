
class Solution:
    def maxSum(self, nums: List[int], k: int) -> int:
        MOD = 10**9 + 7
        bits = [0] * 32

        for num in nums:
            for i in range(32):
                if num & (1 << i):
                    bits[i] += 1

        ans = 0

        for _ in range(k):
            value = 0

            for i in range(32):
                if bits[i] > 0:
                    value |= (1 << i)
                    bits[i] -= 1

            ans = (ans + value * value) % MOD

        return ans
