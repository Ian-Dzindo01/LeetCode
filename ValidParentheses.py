class Solution:
    def isValid(self, s: str) -> bool:

        if len(s)%2 != 0:
            return False

        d = { '{':'}', '[':']', '(':')' }
        brackets = []

        for i in s:

            if i in d.keys():
                brackets += i


            elif i in d.values() and not brackets:     # if brackets are empty
                return False


            elif brackets and i == d[brackets[-1]]:
                brackets.pop()
            else:
                return False

        if brackets:
            return False

        return True
