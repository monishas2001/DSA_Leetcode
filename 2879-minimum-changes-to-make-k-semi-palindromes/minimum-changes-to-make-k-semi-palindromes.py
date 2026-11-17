class Solution:
    def minimumChanges(self, s: str, k: int) -> int:
        n = len(s)
     
        divisors = [[] for _ in range(n + 1)]
        for length in range(1, n + 1):
            for d in range(1, length):
                if length % d == 0:
                    divisors[length].append(d)
        cost = [[inf] * n for _ in range(n)]
        for i in range(n):
            for j in range(i + 1, n):
                length = j - i + 1
                sub = s[i:j+1]
                min_c = inf
                
                for d in divisors[length]:
                    current_cost = 0
                    for start in range(d):
                        group = sub[start::d]
                        m = len(group)
                        for l in range(m // 2):
                            if group[l] != group[m - 1 - l]:
                                current_cost += 1
                    min_c = min(min_c, current_cost)
                
                cost[i][j] = min_c

        memo = {}
        def dp(i, parts):
            if parts == 1:
                return cost[i][n - 1] if n - i >= 2 else inf
            if (i, parts) in memo:
                return memo[(i, parts)]
            
            res = inf
            for m in range(i + 1, n - (parts - 1) * 2 + 1):
                res = min(res, cost[i][m] + dp(m + 1, parts - 1))
                
            memo[(i, parts)] = res
            return res

        return dp(0, k)