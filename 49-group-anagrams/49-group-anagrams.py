class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        hashmap = {}
        for i, str in enumerate(strs):
            sorted_str = tuple(sorted(str))
            if sorted_str in hashmap:
                hashmap[sorted_str].append(i)
            else:
                hashmap[sorted_str] = [i]
                
        answer = []
        for key in hashmap:
            answer.append([strs[i] for i in hashmap[key]])
            
        return answer