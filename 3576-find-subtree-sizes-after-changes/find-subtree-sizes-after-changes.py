class Solution:
    def findSubtreeSizes(self, parent: List[int], s: str) -> List[int]:
        n = len(parent)
        orig_children = [[] for _ in range(n)]
        for node in range(1, n):
            orig_children[parent[node]].append(node)

        new_parent = parent[:]
        last_seen = [-1] * 26  

        def rewire(u: int) -> None:
            idx = ord(s[u]) - ord('a')
            if last_seen[idx] != -1:
                new_parent[u] = last_seen[idx]

            prev_ancestor = last_seen[idx]
            last_seen[idx] = u

            for v in orig_children[u]:
                rewire(v)

            last_seen[idx] = prev_ancestor

        rewire(0)

        final_children = [[] for _ in range(n)]
        for node in range(1, n):
            final_children[new_parent[node]].append(node)

        answer = [0] * n

        def compute_sizes(u: int) -> int:
            size = 1
            for v in final_children[u]:
                size += compute_sizes(v)
            answer[u] = size
            return size

        compute_sizes(0)
        return answer