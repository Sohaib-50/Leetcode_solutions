# The isBadVersion API is already defined for you.
# @param version, an integer
# @return an integer
# def isBadVersion(version):

class Solution:
    def firstBadVersion(self, n):
        """
        :type n: int
        :rtype: int
        """
        low = 1
        high = n
        
        while low <= high:
            mid = (low + high) // 2
            is_bad = isBadVersion(mid)
            if is_bad:
                if mid == 1 or (not isBadVersion(mid - 1)):
                    break
                else:
                    high = mid - 1
            else:
                low = mid + 1
                
        return mid
        