class Solution:
    def findRestaurant(self, list1: List[str], list2: List[str]) -> List[str]:
        list1_map = {}
        for i in range(len(list1)):
            list1_map[list1[i]] = i
            
        min_sum = float('inf')
        answer = []
        
        for i2 in range(len(list2)):
            
            if (i1 := list1_map.get(list2[i2], -1)) != -1:  # if current string exists in list1
                
                if (i1 + i2) < min_sum:
                    answer.clear()
                    min_sum = (i1 + i2)
                    
                if (i1 + i2) <= min_sum:
                    answer.append(list2[i2])
        
        return answer
        