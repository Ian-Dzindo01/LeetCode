class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        s = ''.join([str(i) for i in digits])
        s = int(s)
        s += 1
        return map(int, str(s))
