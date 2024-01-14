class Solution:
    def wordPattern(self, pattern: str, s: str) -> bool:
        d = {}
        ls = s.split()

        if len(pattern) != len(ls):
            return False

        for i in range(len(pattern)):
            if ls[i] in d.values() and pattern[i] not in d.keys():
                return False

            if pattern[i] not in d:
                d[pattern[i]] = ls[i]

        print(d)

        for i in range(len(pattern)):
            if d[pattern[i]] != ls[i]:
                return False

        return True
