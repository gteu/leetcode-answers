# It's a extremely simple solution. Counter() has the method '__eq__'.

class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        return Counter(s) == Counter(t)
        
