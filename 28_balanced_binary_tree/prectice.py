class TreeNode:
    def __init__(self, value = 0, right = None, left = None) -> None:
        self.value = value
        self.right = right
        self.left = left
class Solution:
    def isBalanced(self, root):
        def check_height(node):
            if not node:
                return 0
            left_height = check_height(node.left)
            if left_height == -1:
                return -1
            right_height = check_height(node.right)
            if right_height == -1:
                return -1
            if abs(left_height - right_height) > 1:
                return -1
            return max(left_height , right_height) + 1
        return check_height(root) != -1
root = TreeNode(1)
root.left = TreeNode(2)
root.right = TreeNode(3)
root.left.left = TreeNode(4)
root.left.right = TreeNode(5)
sol = Solution()
print(sol.isBalanced(root))