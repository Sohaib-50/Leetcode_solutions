class Solution:
    def bagOfTokensScore(self, tokens: List[int], power: int) -> int:
        tokens.sort()
        best_score = score = 0
        l = 0
        r = len(tokens) - 1

        while l <= r:
            if power >= tokens[l]:
                score += 1
                best_score = max(best_score, score)
                power -= tokens[l]
                l += 1

            elif score >= 1:
                power += tokens[r]
                r -= 1
                score -= 1
                
            else: 
                break

        return best_score
