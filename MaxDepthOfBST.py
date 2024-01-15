# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        def trav(node):
            if node is None:
                return 0

            else:
                lDepth = trav(node.left)
                rDepth = trav(node.right)

                if (lDepth > rDepth):
                    return lDepth+1
                else:
                    return rDepth+1

        ans = trav(root)
        return ans
