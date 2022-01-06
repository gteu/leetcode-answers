# This is a more intuitive solutions using stack.
# In stack, each value corresponding to each left parenthesis will be the sum inside the parentheses.
# Time O(N), Space O(N)

class Solution:
    def scoreOfParentheses(self, s: str) -> int:
        stack = [0]
        for c in s:
            if c == "(":
                stack.append(0)
            else:
                tmp = stack.pop()
                if tmp != 0:
                    stack[-1] += tmp * 2
                else:
                    stack[-1] += 1
        return stack[0]