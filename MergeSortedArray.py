# compare last 2 initialized elements and place at end of list
class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        p = len(nums1) - 1      # position for element to be inserted
        m = m - 1             # traverse backwards
        n = n - 1             # traverse backwards

        while m >= 0 and n >= 0:
            if nums1[m] >= nums2[n]:
                nums1[p] = nums1[m]
                m -= 1
            else:
                nums1[p] = nums2[n]
                n -= 1

            p -= 1

        if n >= 0:                       # if there are any leftovers
            nums1[:n+1] = nums2[:n+1]
