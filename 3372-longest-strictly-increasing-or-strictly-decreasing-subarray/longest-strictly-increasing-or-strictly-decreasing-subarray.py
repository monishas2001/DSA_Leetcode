class Solution:
    def longestMonotonicSubarray(self, nums: List[int]) -> int:
        maximum=1
        increase=1
        decrease=1
        for i in range(1,len(nums)):
            if nums[i]>nums[i-1]:
                increase+=1
            else:
                increase=1
            if nums[i]<nums[i-1]:
                decrease+=1
            else:
                decrease=1
            maximum = max(maximum,increase, decrease)
        return maximum
