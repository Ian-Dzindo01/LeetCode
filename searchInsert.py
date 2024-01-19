class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:
        if target in nums:
            return nums.index(target)

        index = len(nums)
        # Searching for the position
        for i in range(len(nums)):
            if nums[i] > target:
                index = i
                break
        return index
