class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        string1 = ''.join(sorted(s))
        string2 = ''.join(sorted(t))
        return string1 == string2