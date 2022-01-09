class Solution:
    def countWords(self, words1: List[str], words2: List[str]) -> int:
        wc1, wc2 = Counter(words1), Counter(words2)
        return len(set(k for k, v in wc1.items() if v == 1) & set(k for k, v in wc2.items() if v == 1))
