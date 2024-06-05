class Solution:
    def largestAltitude(self, gain: List[int]) -> int:
        max_altitude = current_altitude = 0
        for i in gain:
            current_altitude += i
            max_altitude = max(max_altitude, current_altitude)
        return max_altitude
