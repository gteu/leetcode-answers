# It is three times faster than answer.py because this solution requires for loop only once.

class Solution:
    def pushDominoes(self, dominoes: str) -> str:
        dominoes = "L" + dominoes + "R"
        i = 0
        ans = ""
        for j in range(1, len(dominoes)):
            if dominoes[j] == ".":
                continue
            mid = j - i - 1
            if dominoes[i] == dominoes[j]:
                ans += dominoes[i] * mid
            elif dominoes[i] == "R" and dominoes[j] == "L":
                ans += "R" * (mid // 2) + "." * (mid % 2) + "L" * (mid // 2)
            else:
                ans += dominoes[i+1:j]
            ans += dominoes[j]
            i = j
        return ans[:-1]
    