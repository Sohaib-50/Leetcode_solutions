class Solution:
    def distributeCandies(self, candyType: List[int]) -> int:
        count_types = len(set(candyType))
        
        allowed_candies = len(candyType) // 2
        
        # answer = 0
        # while count_types > 0 and allowed_candies > 0:
        #     allowed_candies -= 1
        #     count_types -= 1
        #     answer += 1
            
        return min(count_types, allowed_candies)
    