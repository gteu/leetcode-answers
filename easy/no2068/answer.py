class Solution:
    def checkAlmostEquivalent(self, word1: str, word2: str) -> bool:
        wc1, wc2 = Counter(word1), Counter(word2)
        for word in wc1 + wc2:
            if abs(wc1[word] - wc2[word]) > 3:
                return False
        return True
