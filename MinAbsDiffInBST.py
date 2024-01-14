# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def getMinimumDifference(self, root: TreeNode) -> int:
        def trav(root):

            if root is None:              # if at end of tree return
                return

            trav(root.left)
            nonlocal answer, prev          # nonlocal so it can be referenced outside this function
            answer = min(answer, abs(prev - root.val))         # check if new diff is larger than old diff
            prev = root.val

            trav(root.right)

        answer = prev = 100000
        trav(root)                      # initialize the functon
        return answer
