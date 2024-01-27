class Solution:
    def reverseWords(self, s: str) -> str:
        ls = list(s.split(' '))
        ls.reverse()
        ls = list(filter(('').__ne__, ls))
        res = ' '.join(word for word in ls)
        return res
