class Solution:
    def maximumSaleItems(self, items: List[List[int]], budget: int) -> int:
        max_factor = max(factor for factor, _ in items)
        freq = [0] * (max_factor + 1)
        for factor, _ in items:
            freq[factor] += 1

        factor_bonus = [0] * (max_factor + 1)
        for f in range(1, max_factor + 1):
            if freq[f] == 0:
                continue
            multiples_count = 0
            for multiple in range(f, max_factor + 1, f):
                multiples_count += freq[multiple]
 
            factor_bonus[f] = multiples_count - 1

        dp = [0] * (budget + 1)

        for factor, price in items:
            if price > budget:
                continue
            bonus = factor_bonus[factor]

            first_gain = 1 + bonus
            for b in range(budget, price - 1, -1):
                if dp[b - price] + first_gain > dp[b]:
                    dp[b] = dp[b - price] + first_gain

            for b in range(price, budget + 1):
                if dp[b - price] + 1 > dp[b]:
                    dp[b] = dp[b - price] + 1

        return max(dp)