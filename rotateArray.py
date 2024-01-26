from collections import deque

class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
        n = len(nums)
        k = k % n  # ensure k is within the range of array size
        nums = nums[-k:] + nums[:-k]
        print(nums)
