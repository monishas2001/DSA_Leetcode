class Solution:
    def smallestUniqueSubarray(self, nums: List[int]) -> int:
        n = len(nums)
   
        base1, mod1 = 100003, 10**9 + 7
        base2, mod2 = 100019, 10**9 + 9

        pow1 = [1] * (n + 1)
        pow2 = [1] * (n + 1)
        pref1 = [0] * (n + 1)
        pref2 = [0] * (n + 1)

        for i, val in enumerate(nums):
            pow1[i + 1] = (pow1[i] * base1) % mod1
            pow2[i + 1] = (pow2[i] * base2) % mod2
            pref1[i + 1] = (pref1[i] * base1 + val) % mod1
            pref2[i + 1] = (pref2[i] * base2 + val) % mod2

        def has_unique_of_length(length: int) -> bool:
            counts = Counter()
            for start in range(n - length + 1):
                end = start + length
                h1 = (pref1[end] - pref1[start] * pow1[length]) % mod1
                h2 = (pref2[end] - pref2[start] * pow2[length]) % mod2
                counts[(h1, h2)] += 1

            return any(freq == 1 for freq in counts.values())

        low, high = 1, n
        ans = n
        while low <= high:
            mid = (low + high) // 2
            if has_unique_of_length(mid):
                ans = mid
                high = mid - 1
            else:
                low = mid + 1

        return ans