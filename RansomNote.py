from collections import Counter
# cant use sets because count of letter matters
# iterate through the 2 dicts and check if both have letters
class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        d1 = Counter(ransomNote)
        d2 = Counter(magazine)
        for i in d1.keys():
            if i in d2.keys():
                d2[i] = d2[i] - d1[i]
                if d2[i] < 0:
                    return False
            else:
                return False

        return True
