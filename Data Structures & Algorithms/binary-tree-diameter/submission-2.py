# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        #Length is the biggest distance between nodes in the tree.
        self.curr = 0 #{node:distance from root}
        def walker(node):
            if not node:
                return 0
            
            left = walker(node.left)
            right = walker(node.right)

            self.curr = max(self.curr, left + right)
            return 1 + max(left,right)

        walker(root)
              


        return self.curr

        