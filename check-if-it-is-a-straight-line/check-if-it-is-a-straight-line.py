class Solution:
    def checkStraightLine(self, coordinates: List[List[int]]) -> bool:
        # gradient of first 2 coordinates
        if (coordinates[0][0] - coordinates[1][0]) == 0:
            first_gradient = float('inf')
        else:
            first_gradient = (coordinates[0][1] - coordinates[1][1]) / (coordinates[0][0] - coordinates[1][0])
        
        # check of gradient of first and current coordinate is same as first 2 coordinates for all coordinates after 2nd coordinate
        for current_coordinate in coordinates[2:]:
            if (coordinates[0][0] - current_coordinate[0]) == 0:
                current_gradient = float('inf')
            else:
                current_gradient = (coordinates[0][1] - current_coordinate[1]) / (coordinates[0][0] - current_coordinate[0])

            if current_gradient != first_gradient:
                return False
            
        return True