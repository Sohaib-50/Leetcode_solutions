class Solution:
    def checkIfExist(self, arr: List[int]) -> bool:
        arr_set = set()
        
        for i in arr:
            if (i * 2 in arr_set) or (i / 2 in arr_set):
                return True
            arr_set.add(i)
            
        return False