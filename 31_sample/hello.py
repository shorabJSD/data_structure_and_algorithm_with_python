class TreeNode:
  def __init__(self,  value = 0, right = None, left = None):
    self.value = value
    self.right = right
    self.left  = left
def hasDepthSum(root, targetSum):
  if not root:
    return 