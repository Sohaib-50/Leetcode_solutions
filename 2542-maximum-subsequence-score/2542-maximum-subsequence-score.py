class Solution:
    def maxScore(self, nums1: List[int], nums2: List[int], k: int) -> int:
        import heapq

        heap = []  # minheap for nums1 values
        sum_nums1 = 0  # sum of nums1 values in heap
        max_score = 0

        pairs = [(nums2[i], nums1[i]) for i in range(len(nums1))]
        pairs.sort(reverse=True)
        print(pairs)

        for num2, num1 in pairs:
            heapq.heappush(heap, num1)
            sum_nums1 += num1

            # keep heap to k elements
            if len(heap) > k:
                sum_nums1 -= heapq.heappop(heap)

            if len(heap) == k:
                score = sum_nums1 * num2
                max_score = max(max_score, score)

        return max_score

