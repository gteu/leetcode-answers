class Solution:
    def countWordInList(self, words):
        wc = {}
        for word in words:
            if word not in wc.keys():
                wc[word] = 1
            else:
                wc[word] += 1
        return wc
    
    def countWords(self, words1: List[str], words2: List[str]) -> int:
        wc1, wc2 = self.countWordInList(words1), self.countWordInList(words2)
        ans = 0
        for key, value in wc1.items():
            if value == 1 and wc2.get(key) == 1:
                ans += 1
        return ans
