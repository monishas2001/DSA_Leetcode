class Solution:
    def minimumSumSubarray(self, nums: List[int], l: int, r: int) -> int:
        minimum = float('inf')

        for i in range(len(nums)):
            total = 0

            for j in range(i, len(nums)):
                total += nums[j]

                length = j - i + 1

                if l <= length <= r and total > 0:
                    minimum = min(minimum, total)

        if minimum == float('inf'):
            return -1

        return minimum