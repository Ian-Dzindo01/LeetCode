from collections import Counter

class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        cnt = Counter(list(nums))
        m = max(cnt.values())
        return (list(cnt.keys())[list(cnt.values()).index(m)])
