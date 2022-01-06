# This is a more concise solutions with O(1) memory.
# Only when "()" appears, it adds the score.
# Example: Given s = "(()(()())())", the equation will be like "(1 + (1 + 1) * 2 + 1) * 2".
# You will tell from this when "()" appears, you should add 2 to the power of its depth.


class Solution:
    def scoreOfParentheses(self, s: str) -> int:
        h, ans = 0, 0
        for i in range(len(s)):
            if s[i] == "(":
                h += 1
            else:
                if s[i-1] == "(":
                    ans += 2**(h-1)
                h -= 1
        return ans