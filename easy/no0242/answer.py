class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        cs, ct = Counter(s), Counter(t)
        for cs_key in cs.keys():
            if cs[cs_key] != ct[cs_key]:
                return False
        for ct_key in ct.keys():
            if cs[ct_key] != ct[ct_key]:
                return False
        return True
        
