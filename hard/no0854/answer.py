# By thinking of each string as node, use BFS to solve the shortest path.
# In each step, there will be O(n^2) ways to swap, resulting in TLE.
# If you swap each element to make the other string from left to right, they are reduced to O(n) ways.
# But, i don't fully understand why this greedy-like solution will be optimal.

from collections import deque

class Solution:
    def kSimilarity(self, s1: str, s2: str) -> int:
        if s1 == s2:
            return 0
        queue = deque([s1])
        seen = {s1: 0}
        while queue:
            s = queue.popleft()
            count = seen[s]
            for i in range(len(s)-1):
                if s[i] != s2[i]:
                    for j in range(i+1, len(s)):
                        if s[j] == s2[i] and s[j] != s2[j]:
                            next_s = s[:i] + s[j] + s[i+1:j] + s[i] + s[j+1:]
                            if seen.get(next_s):
                                continue
                            if next_s == s2:
                                return count + 1
                            queue.append(next_s)
                            seen[next_s] = count + 1
                    break