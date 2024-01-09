class Solution:
    def romanToInt(self, s: str) -> int:
        res, i = 0, 0
        d1 = {'I':1, 'V':5, 'X':10, 'L':50, 'C':100, 'D':500, 'M':1000}
        d2 = {'IV':4, 'IX':9, 'XL':40, 'XC':90, 'CD':400, 'CM':900}

        while(True):
            if i >= len(s):
                break
            if s[i:i+2] in d2.keys():
                res += d2[s[i:i+2]]
                i += 2
                continue

            res += d1[s[i]]
            print(i)
            i += 1

        return res
