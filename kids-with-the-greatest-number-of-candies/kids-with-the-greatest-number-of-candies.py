class Solution:
    def kidsWithCandies(self, candies: List[int], extraCandies: int) -> List[bool]:
        # find out what's the max candies any child currently has
        max_candies = 1
        for candy in candies:
            max_candies = max(max_candies, candy)
        
        
        # if a child is given all the extra candies and that makes his candies same as or more than the max candies then the yes they have max candies out of all after recieving those extra candies.
        ans = [False for candy in candies]  # initialize array of candies size, with False for all childeren
        for i in range(len(candies)):
            if (candies[i] + extraCandies) >= max_candies:  # if giving extra candies to child makes them have same or more candies than the max candy guy (originally)
                ans[i] = True
                
        
        return ans