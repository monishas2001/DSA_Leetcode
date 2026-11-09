class Solution:
    def busiestServers(self, k: int, arrival: list[int], load: list[int]) -> list[int]:
        busy = []
        import sortedcontainers 
        available = sortedcontainers.SortedList(range(k))
        
        requests_handled = [0] * k
        
        for i, (arr_time, l_time) in enumerate(zip(arrival, load)):
            while busy and busy[0][0] <= arr_time:
                _, server_id = heapq.heappop(busy)
                available.add(server_id)
            if not available:
                continue
            preferred = i % k
            idx = available.bisect_left(preferred)
            if idx == len(available):
                idx = 0
            
            server_id = available[idx]
            
            available.remove(server_id)
            heapq.heappush(busy, (arr_time + l_time, server_id))
            requests_handled[server_id] += 1
        max_handled = max(requests_handled)
        return [i for i, count in enumerate(requests_handled) if count == max_handled]