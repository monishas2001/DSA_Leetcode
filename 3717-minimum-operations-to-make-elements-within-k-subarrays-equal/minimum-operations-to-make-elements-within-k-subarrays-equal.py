
from typing import List

class Fenwick:
    def __init__(self, n):
        self.n = n
        self.tree = [0] * (n + 1)

    def add(self, i, val):
        i += 1
        while i <= self.n:
            self.tree[i] += val
            i += i & -i

    def query(self, i):
        i += 1
        res = 0
        while i > 0:
            res += self.tree[i]
            i -= i & -i
        return res

    def kth(self, k):
        idx = 0
        bit = 1 << (self.n.bit_length() - 1)

        while bit:
            nxt = idx + bit
            if nxt <= self.n and self.tree[nxt] < k:
                idx = nxt
                k -= self.tree[nxt]
            bit >>= 1

        return idx
any 

class Solution:
    def minOperations(self, nums: List[int], x: int, k: int) -> int:
        n = len(nums)

        vals = sorted(set(nums))
        size = len(vals)

        pos = {v: i for i, v in enumerate(vals)}

        count = Fenwick(size)
        sums = Fenwick(size)

        total = 0

        def add(v, sign):
            nonlocal total
            idx = pos[v]
            count.add(idx, sign)
            sums.add(idx, v * sign)
            total += v * sign

        # Initialize first window
        for i in range(x):
            add(nums[i], 1)

        costs = [0] * (n + 1)

        # Calculate cost of every window
        for end in range(x, n + 1):

            mid = count.kth((x + 1) // 2)
            median = vals[mid]

            left_count = count.query(mid)
            left_sum = sums.query(mid)

            right_count = x - left_count
            right_sum = total - left_sum

            cost = (
                median * left_count - left_sum
                + right_sum - median * right_count
            )

            costs[end] = cost

            # Slide the window
            if end < n:
                add(nums[end - x], -1)
                add(nums[end], 1)

        # DP: minimum cost to select j windows
        INF = float('inf')

        prev = [0] * (n + 1)

        for j in range(1, k + 1):
            curr = [INF] * (n + 1)

            for i in range(1, n + 1):

                # Do not select a window ending at i
                curr[i] = curr[i - 1]

                # Select window [i-x, i-1]
                if i >= x:
                    curr[i] = min(
                        curr[i],
                        prev[i - x] + costs[i]
                    )

            prev = curr

        return prev[n]
