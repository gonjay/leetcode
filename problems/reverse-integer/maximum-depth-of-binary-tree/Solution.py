# Definition for a  binary tree node
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    # @param root, a tree node
    # @return an integer
    def __init__(self):
        self.arr = []
        self.maxdepth = 0

    def maxDepth(self, root):
        self.mapTree(root)
        return self.maxdepth

    def mapTree(self, node):
        if node is None:
            return None
        self.arr.append(node)
        self.maxdepth = len(self.arr) if self.maxdepth < len(self.arr) else self.maxdepth
        left = node.left
        right = node.right
        while left:
            self.mapTree(left)
            self.arr.pop()
            break
        while right:
            self.mapTree(right)
            self.arr.pop()
            break