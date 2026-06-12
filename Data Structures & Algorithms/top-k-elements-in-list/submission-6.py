class Solution:
    # {1:1, 2:2, 3:3}
    # [(2,2)(3,3)]
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        counter = Counter(nums) 

        minHeap = []
        res = []

        for key, val in counter.items():
            heapq.heappush(minHeap, (val, key))
            if len(minHeap) > k:
                heapq.heappop(minHeap)

        for item in minHeap:
            res.append(item[1])

        return res

    

    
