class Solution:
    def mostCommonWord(self, paragraph: str, banned: List[str]) -> str:
        counts = {}
        current_word = ""
        terminators = {" ", "!", "?", ",", ";", ".", "'", '"'}
        for char in paragraph:
            if (char in terminators):
                if current_word:
                    current_word = current_word.lower()
                    if current_word not in banned:
                        counts[current_word] = counts.get(current_word, 0) + 1
                current_word = ""
            else:
                current_word += char
        
        if current_word:
            current_word = current_word.lower()
            if current_word not in banned:
                counts[current_word] = counts.get(current_word, 0) + 1
            
        max_count = float("-inf")
        for word in counts:
            max_count = max(max_count, counts[word])
            
        for word in counts:
            if counts[word] == max_count:
                return word