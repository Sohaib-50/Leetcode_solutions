class Solution:
    def arithmeticTriplets(self, nums: List[int], diff: int) -> int:
        # answer = []
        answer = 0
        lookup = {}
        for i in range(len(nums)):
            lookup[nums[i]] = i
        
        for i in range(len(nums) - 1):
            for j in range(i + 1, len(nums)):
                if (nums[j] - nums[i]) == diff:
                    if lookup.get(diff + nums[j], -1) > j:
                        # answer.append((i, j, lookup[diff + nums[j]]))
                        answer += 1
        # print(answer)
        
        # return len(answer)
        return answer