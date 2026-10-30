class Solution:
    def shortestPath(self, n: int, edges: List[List[int]], labels: str, k: int) -> int:
        graph = [[] for _ in range(n)]
        for u, v, w in edges:
            graph[u].append((v, w))
        dist = [[float('inf')] * (k + 1) for _ in range(n)]
        dist[0][1] = 0
        pq = [(0, 0, 1)] 
        
        while pq:
            curr_w, u, consec = heapq.heappop(pq)
            if u == n - 1:
                return curr_w
            if curr_w > dist[u][consec]:
                continue
                
            for v, weight in graph[u]:
                if labels[v] == labels[u]:
                    next_consec = consec + 1
                else:
                    next_consec = 1
                    
                if next_consec <= k:
                    if curr_w + weight < dist[v][next_consec]:
                        dist[v][next_consec] = curr_w + weight
                        heapq.heappush(pq, (curr_w + weight, v, next_consec))
                        
        return -1