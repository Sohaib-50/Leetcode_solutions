class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        from heapq import heappop, heappush

        min_heap = []
        for num in nums:

            if len(min_heap) < k:
                heappush(min_heap, num)
                continue

            if num > min_heap[0]:
                heappop(min_heap)
                heappush(min_heap, num) 
            

        return min_heap[0]
