class Solution:
    def sumCounts(self, nums: List[int]) -> int:
        total=0
        for i in range(len(nums)):
            for j in range(i+1,len(nums)+1):
                subarray = nums[i:j]
                distinct_count = len(set(subarray))
                total += distinct_count ** 2

        return total


        