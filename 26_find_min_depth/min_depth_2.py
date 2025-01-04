from collections import deque

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

def minDepth(root):
    # If the tree is empty, return 0 as there are no nodes.
    if not root:
        return 0

    # Initialize a queue for level-order traversal. Each element in the queue
    # is a tuple containing a node and its depth in the tree.
    queue = deque([(root, 1)])

    while queue:
        # Pop the front element from the queue.
        node, depth = queue.popleft()

        # If the current node is a leaf (no children), return its depth.
        if not node.left and not node.right:
            return depth

        # If the current node has a left child, add it to the queue with depth + 1.
        if node.left:
            queue.append((node.left, depth + 1))

        # If the current node has a right child, add it to the queue with depth + 1.
        if node.right:
            queue
            
            queue.append((node.right, depth + 1))
root = TreeNode(1)
root.left = TreeNode(2, TreeNode(4), TreeNode(5))
root.right = TreeNode(3)
print(minDepth(root))