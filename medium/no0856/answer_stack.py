# This is a solution using stack.
# The variable cur has the current sum of the score, and the element of each stack has the cur value when it's inserted.
# Time O(N), Space O(N)

class Solution:
    def scoreOfParentheses(self, s: str) -> int:
        stack = []
        cur = 0
        for c in s:
            if c == "(":
                stack.append(cur)
                cur = 0
            else:
                cur += stack.pop() + max(cur, 1)
        return cur