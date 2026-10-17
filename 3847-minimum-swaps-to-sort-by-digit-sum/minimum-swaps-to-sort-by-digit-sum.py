class Solution:
    def minSwaps(self, nums: List[int]) -> int:
        arr = sorted(nums, key=lambda x: (sum(int(d) for d in str(x)), x))

        pos = {num: i for i, num in enumerate(nums)}
        swaps = 0

        for i in range(len(nums)):
            if nums[i] != arr[i]:
                j = pos[arr[i]]

                pos[nums[i]] = j
                pos[arr[i]] = i

                nums[i], nums[j] = nums[j], nums[i]
                swaps += 1

        return swaps