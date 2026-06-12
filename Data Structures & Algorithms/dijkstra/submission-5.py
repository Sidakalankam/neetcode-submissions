class Solution:
    def shortestPath(self, n: int, edges: List[List[int]], src: int) -> Dict[int, int]:
        adj = {}

        for i in range(n):
            adj[i] = []

        for u, v, w in edges:
            adj[u].append((v, w))

        shortest_paths = {}

        minHeap = [(0, src)]

        while minHeap:
            w1, n1 = heapq.heappop(minHeap)
            if n1 in shortest_paths:
                continue
            shortest_paths[n1] = w1

            for n2, w2 in adj[n1]:
                if n2 not in shortest_paths:
                    heapq.heappush(minHeap, (w1 + w2, n2))

        for i in range(n):
            if i not in shortest_paths:
                shortest_paths[i] = -1
                    
        return shortest_paths

        