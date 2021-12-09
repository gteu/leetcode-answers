class Solution:
    def titleToNumber(self, ct: str) -> int:
        n = len(ct)
        ans = 0
        for i in range(n):
            ans += 26 ** (n - i - 1) * (ord(ct[i]) - ord("A") + 1)
        return ans
            
