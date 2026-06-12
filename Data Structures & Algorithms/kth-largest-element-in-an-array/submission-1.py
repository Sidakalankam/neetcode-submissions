class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        maxHeap = [-val for val in nums]
        heapq.heapify(maxHeap)

        while k > 0:
            res = heapq.heappop(maxHeap)
            if k == 1:
                return -res
            k -= 1
    
