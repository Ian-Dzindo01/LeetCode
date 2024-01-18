# loop through each value in the list
class Solution:
    def containsNearbyDuplicate(self, nums, k):
        l = {}
        for i, val in enumerate(nums):
            if val not in l:
                l[val] = i
            else:
                if i - l[val] <= k:
                    return True
                l[val] = i
        return False
