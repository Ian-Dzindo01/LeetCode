class Solution:
    def isIsomorphic(self, s: str, t: str) -> bool:
        d = {}
        for i in range(len(s)):
            if s[i] not in d.keys() and t[i] in d.values():
                return False
            if s[i] not in d:
                d[s[i]] = t[i]
            else:
                if t[i] != d[s[i]]:
                    return False

        print(d)
        return True
