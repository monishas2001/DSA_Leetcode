class Solution:
    def minSumSquareDiff(self, nums1: list[int], nums2: list[int], k1: int, k2: int) -> int:
        diffs = [abs(a - b) for a, b in zip(nums1, nums2)]
        k = k1 + k2
        if sum(diffs) <= k:
          return 0

        left, right = 0, max(diffs)

        while left < right:
            mid = (left + right) // 2
            needed = sum(max(0, d - mid) for d in diffs)

            if needed <= k:
                right = mid
            else:
                left = mid + 1

        limit = left
        remaining = k - sum(max(0, d - limit) for d in diffs)

        ans = 0

        for d in diffs:
            d = min(d, limit)

            if remaining > 0 and d == limit and limit > 0:
                d -= 1
                remaining -= 1

            ans += d * d

        return ans