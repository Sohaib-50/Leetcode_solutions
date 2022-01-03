class Solution:
    def findJudge(self, n: int, trust: List[List[int]]) -> int:
        incoming_edges = [0 for i in range(n)]
        outgoing_edges = [0 for i in range(n)]
        
        
        for trust in trust:
            outgoing_edges[trust[0] - 1] += 1
            incoming_edges[trust[1] - 1]  += 1
            
        for i in range(n):
            if (incoming_edges[i] == (n - 1)) and (outgoing_edges[i] == 0):
                return i + 1
            
        return -1