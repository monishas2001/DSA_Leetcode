from typing import List

class Solution:
    def sumCounts(self, nums: List[int]) -> int:
        MOD = 10**9 + 7
        n = len(nums)

        total = [0] * (4 * n)
        sq = [0] * (4 * n)
        lazy = [0] * (4 * n)

        def update(node, start, end, left, right):
            if left <= start and end <= right:
                length = end - start + 1
                sq[node] = (sq[node] + 2 * lazy[node] * total[node]
                            + lazy[node] * lazy[node] * length) % MOD
                total[node] = (total[node] + lazy[node] * length) % MOD
                return

            mid = (start + end) // 2
            if left <= mid:
                update(node * 2, start, mid, left, right)
            if right > mid:
                update(node * 2 + 1, mid + 1, end, left, right)

            total[node] = (total[node * 2] + total[node * 2 + 1]) % MOD
            sq[node] = (sq[node * 2] + sq[node * 2 + 1]) % MOD

        def add(node, start, end, left, right):
            if left <= start and end <= right:
                length = end - start + 1
                sq[node] = (sq[node] + 2 * total[node] + length) % MOD
                total[node] = (total[node] + length) % MOD
                lazy[node] += 1
                return

            mid = (start + end) // 2

            if lazy[node]:
                for child, lo, hi in (
                    (node * 2, start, mid),
                    (node * 2 + 1, mid + 1, end)
                ):
                    length = hi - lo + 1
                    d = lazy[node]
                    sq[child] = (sq[child] + 2 * d * total[child]
                                 + d * d * length) % MOD
                    total[child] = (total[child] + d * length) % MOD
                    lazy[child] += d
                lazy[node] = 0

            if left <= mid:
                add(node * 2, start, mid, left, right)
            if right > mid:
                add(node * 2 + 1, mid + 1, end, left, right)

            total[node] = (total[node * 2] + total[node * 2 + 1]) % MOD
            sq[node] = (sq[node * 2] + sq[node * 2 + 1]) % MOD

        last = {}
        ans = 0

        for i, x in enumerate(nums):
            prev = last.get(x, -1)
            add(1, 0, n - 1, prev + 1, i)
            last[x] = i
            ans = (ans + sq[1]) % MOD

        return ans