# iterate and select the remainder of the list reachable by nums[i]
# take max of that list and jump to that number
# keep a cnt variable to count number of jumps you have to take

class Solution:
    def jump(self, nums: List[int]) -> int:
        res,l,r = 0,0,0        # represents window of array for BFS
        while r < len(nums)-1:
            f = 0
            for i in range(l, r+1):         # find largest jump you can make
                f = max(f,i+nums[i])

            l = r+1                # move to next section
            r = f                  # move right pointer to farthest jump
            res += 1

        return res

