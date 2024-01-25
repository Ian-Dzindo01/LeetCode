class Solution:
    def canJump(self, nums: List[int]) -> bool:
        tmp = 0
        for i in range(len(nums)-1):
            tmp -= 1

            if tmp <= nums[i]:
                tmp = nums[i]

            if nums[i] == 0 and tmp <= 0:
                return False

        return True
