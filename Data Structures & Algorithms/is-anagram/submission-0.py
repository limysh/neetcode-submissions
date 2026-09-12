from collections import defaultdict
class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
        
        a,b = defaultdict(int), defaultdict(int)
        for i in range(len(s)):
            a[s[i]] += 1
            b[t[i]] += 1
        if a == b:
            return True
        else:
            return False


        