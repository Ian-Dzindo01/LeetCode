class Solution:
    def isHappy(self, n: int) -> bool:
        cnt = 0
        while(True):
            l = list(str(n))
            r = sum(int(i)**2 for i in l)

            if r == 1:
                return True
                break

            if cnt == 7:
                return False

            n = r
            cnt += 1

