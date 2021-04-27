class Solution:
    def duplicateZeros(self, arr: List[int]) -> None:
        """
        Do not return anything, modify arr in-place instead.
        """
        l = len(arr)
        i = 0
        while i < l:
            if arr[i] == 0:
                j = l - 1
                while j > i:
                    arr[j] = arr[j - 1]
                    j -= 1
                arr[i] = 0
                i += 1
            # print(arr)
            i += 1
                
            