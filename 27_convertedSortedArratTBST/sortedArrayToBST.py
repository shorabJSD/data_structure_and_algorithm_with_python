class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

def sortedArrayToBST(nums):
    if not nums:
        return None  # Base case: return None for an empty array
    
    mid = len(nums) // 2
    root = TreeNode(nums[mid])  # Create a new TreeNode with the middle element
    root.left = sortedArrayToBST(nums[:mid])  # Recursively build the left subtree
    root.right = sortedArrayToBST(nums[mid + 1:])  # Recursively build the right subtree
    return root

def preorderTraversel(root):
    if not root:
        return []  # Return an empty list for None nodes
    return [root.val] + preorderTraversel(root.left) + preorderTraversel(root.right)

# Example usage
nums = [-10, -3, 0, 5, 9]
root = sortedArrayToBST(nums)
print(preorderTraversel(root))  # Output: Preorder traversal of the BST

