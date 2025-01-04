class TreeNode:
    def __init__(self, value = 0, right = None, left = None):
        self.value = value
        self.right = right
        self.left = left
def hasPathSum(root, targetSum):
    if not root:
        return False
    if not root.left and not root.right:
        return root.value == targetSum
    newSum = root.value - targetSum
    return hasPathSum(root.left, newSum), hasPathSum(root.right, newSum)
root = TreeNode(1)
root.right = TreeNode(2)
root.left = TreeNode(3)
root.left.left = TreeNode(4)
print() 