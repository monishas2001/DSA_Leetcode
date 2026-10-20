class Solution:
    def sortableIntegers(self, nums: list[int]) -> int:
        n = len(nums)
        sorted_nums = sorted(nums)

        def is_rotation(a, b):
            m = len(a)

            # Build KMP prefix table for b
            pi = [0] * m
            j = 0

            for i in range(1, m):
                while j > 0 and b[i] != b[j]:
                    j = pi[j - 1]

                if b[i] == b[j]:
                    j += 1

                pi[i] = j

            # Search for b inside the circular array a
            j = 0

            for i in range(2 * m - 1):
                x = a[i % m]

                while j > 0 and x != b[j]:
                    j = pi[j - 1]

                if x == b[j]:
                    j += 1

                if j == m:
                    return True

            return False

        answer = 0

        for k in range(1, n + 1):
            if n % k != 0:
                continue

            for start in range(0, n, k):
                a = nums[start:start + k]
                b = sorted_nums[start:start + k]

                if not is_rotation(a, b):
                    break
            else:
                answer += k

        return answer