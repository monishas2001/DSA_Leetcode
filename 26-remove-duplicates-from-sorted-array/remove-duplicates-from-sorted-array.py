class Solution:
    def removeDuplicates(self, nums: list[int]) -> int:
        num = []

        for i in range(len(nums)):
            if nums[i] not in num:
                num.append(nums[i])

        k = len(num)
        nums[:k] = num

        return k
