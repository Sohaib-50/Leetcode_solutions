class Solution:
    def largestAltitude(self, gain: List[int]) -> int:
        current_altitude =  max_altitude = 0
        for i in gain:
            current_altitude += i
            max_altitude = max(current_altitude, max_altitude)
            
        return max_altitude