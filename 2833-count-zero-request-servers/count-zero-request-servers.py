class Solution:
    def countServers(self, n: int, logs: List[List[int]], x: int, queries: List[int]) -> List[int]:
            logs.sort(key=lambda log: log[1])
            
            # 2. Sort queries while keeping track of their original indices
            sorted_queries = sorted(enumerate(queries), key=lambda q: q[1])
            
            ans = [0] * len(queries)
            server_request_count = {}
            
            left = 0
            right = 0
            total_logs = len(logs)
            
            # 3. Process each query using a sliding window on logs
            for original_index, q_time in sorted_queries:
                window_start = q_time - x
                window_end = q_time
                
                # Expand window to include logs up to window_end
                while right < total_logs and logs[right][1] <= window_end:
                    server_id = logs[right][0]
                    server_request_count[server_id] = server_request_count.get(server_id, 0) + 1
                    right += 1
                    
                # Shrink window from the left to remove logs older than window_start
                while left < total_logs and logs[left][1] < window_start:
                    server_id = logs[left][0]
                    server_request_count[server_id] -= 1
                    if server_request_count[server_id] == 0:
                        del server_request_count[server_id]
                    left += 1
                    
                # Zeros = Total servers (n) - Servers that received at least one request
                ans[original_index] = n - len(server_request_count)
                
            return ans