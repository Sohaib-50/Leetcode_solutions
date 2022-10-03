class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        hashmap = {}
        for s in strs:
            sorted_str = tuple(sorted(s))
            if sorted_str in hashmap:
                hashmap[sorted_str].append(s)
            else:
                hashmap[sorted_str] = [s]
                
        answer = []
        for key in hashmap:
            answer.append(hashmap[key])
            
        return answer