class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        res = []
        if len(strs) == 1 or len(set(strs)) == 1:
            return strs[0]

        for i in range(1, len(strs[0])+1):
            pref = strs[0][:i]
            print(pref)
            for s in strs:
                if s[:i] != pref:
                    return res[-1] if res else ""

            print(res)
            res.append(pref)

        return res[-1] if res else ""
