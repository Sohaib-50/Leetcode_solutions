class Solution:
    def totalCost(self, costs: List[int], k: int, candidates: int) -> int:
        from heapq import heappush, heappop

        cost = 0
        left_ptr = 0
        right_ptr = len(costs) - 1
        left_minheap = []
        right_minheap = []

        # Initial heaps filling
        for _ in range(candidates):
            
            # workers exhausted
            if left_ptr >= right_ptr:
                if left_ptr == right_ptr:
                    heappush(left_minheap, costs[left_ptr])
                    left_ptr += 1
                break

            heappush(left_minheap, costs[left_ptr])
            left_ptr += 1

            heappush(right_minheap, costs[right_ptr])
            right_ptr -= 1

        # print(left_ptr, right_ptr, len(costs))

        # print(f"Left: {left_minheap}; Right: {right_minheap}\n")

        for _ in range(k):
            left_min = left_minheap[0] if left_minheap else -1
            right_min = right_minheap[0] if right_minheap else -1

            if left_min == right_min == -1:
                break

            choose_right_min = (right_min != -1) and ((right_min < left_min) or (left_min == -1))

            if choose_right_min:
                # print(f"Choosing {right_min} from right")
                heappop(right_minheap)
                cost += right_min

                # add worker if any left
                if right_ptr >= left_ptr:
                    heappush(right_minheap, costs[right_ptr])
                    right_ptr -= 1

            else:  # left_min <= right_min:
                # print(f"Choosing {left_min} from left")
                heappop(left_minheap)
                cost += left_min

                # add worker if any left
                if left_ptr <= right_ptr:
                    heappush(left_minheap, costs[left_ptr])
                    left_ptr += 1

            # print(f"Left: {left_minheap}; Right: {right_minheap}\n")
        
        return cost
