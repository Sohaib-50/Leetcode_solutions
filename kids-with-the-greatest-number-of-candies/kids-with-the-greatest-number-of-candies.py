class Solution:
    def kidsWithCandies(self, candies: List[int], extraCandies: int) -> List[bool]:
        current_max = max(candies)
        ans = []
        for candy in candies:
            ans.append(candy + extraCandies >= current_max)
        return ans
