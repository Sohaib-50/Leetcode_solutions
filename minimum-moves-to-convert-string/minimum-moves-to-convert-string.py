class Solution:
    def minimumMoves(self, s: str) -> int:
        n = len(s)
        i = 0
        moves = 0
        while i < n:
            if s[i] == "X":
                i += 3
                moves += 1
            else:
                i += 1
        return moves