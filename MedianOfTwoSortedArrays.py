class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        lst = nums1 + nums2
        lst.sort()
        mid = len(lst)//2
        res = (lst[mid] + lst[~mid]) / 2
        return res
