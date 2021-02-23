class Solution:
    def countGoodTriplets(self, arr: List[int], a: int, b: int, c: int) -> int:
        count_triplets = 0
        for i in range(len(arr)):
            for j in range(i + 1, len(arr)):
                for k in range(j + 1, len(arr)):
                    if (abs(arr[i] - arr[j]) <= a) and (abs(arr[j] - arr[k]) <= b) and (abs(arr[i] - arr[k]) <= c):
                    # if all((abs(arr[i] - arr[j]) <= a, abs(arr[j] - arr[k]) <= b, abs(arr[i] - arr[k]) <= c)):
                        count_triplets += 1
                        
        return count_triplets
                        