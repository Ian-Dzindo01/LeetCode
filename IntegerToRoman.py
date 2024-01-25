class Solution:
    def intToRoman(self, num: int) -> str:
        syms = [(1000, 'M'), (900, 'CM'),
                        (500, 'D'), (400, 'CD'),
                        (100, 'C'), (90, 'XC'),
                        (50, 'L'), (40, 'XL'),
                        (10, 'X'), (9, 'IX'),
                        (5, 'V'), (4, 'IV'),
                        (1, 'I')]
        res = []

        for val, symbol in syms:
            if num == 0:                # if nothing keft to divide we are at end
                break

            count, num = divmod(num, val)

            res.append(symbol * count)

        return ''.join(res)
