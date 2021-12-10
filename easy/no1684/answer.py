class Solution:
    def countConsistentStrings(self, allowed: str, words: List[str]) -> int:
        count = 0
        for word in words:
            for c in word:
                if c not in allowed:
                    count += 1
                    break
        return len(words) - count