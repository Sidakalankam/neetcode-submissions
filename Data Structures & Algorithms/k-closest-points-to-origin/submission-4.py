class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        res = []
        heap = []
        
        for point in points:
            distance = point[0]**2 + point[1]**2
            heapq.heappush(heap, (distance, point))
        
        while k > 0:
            res.append(heapq.heappop(heap)[1])
            k -= 1
        
        return res
