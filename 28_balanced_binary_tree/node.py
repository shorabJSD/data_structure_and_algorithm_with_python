class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val  # Value of the node
        self.left = left  # Left child node
        self.right = right  # Right child node

class Solution:
    def isBalanced(self, root):
        # Helper function to calculate height and check balance
        def check_height(node):
            if not node:  # Base case: An empty tree is balanced
                return 0  # Height of an empty tree is 0

            # Recursively check the height of the left subtree
            left_height = check_height(node.left)
            if left_height == -1:  # If left subtree is unbalanced
                return -1

            # Recursively check the height of the right subtree
            right_height = check_height(node.right)
            if right_height == -1:  # If right subtree is unbalanced
                return -1

            # If the height difference of subtrees is more than 1, return -1 (not balanced)
            if abs(left_height - right_height) > 1:
                return -1

            # Return the height of the current node
            return max(left_height, right_height) + 1

        # Call the helper function and check if the tree is balanced
        return check_height(root) != -1
