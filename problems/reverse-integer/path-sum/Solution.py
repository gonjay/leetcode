# Definition for a  binary tree node
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    arr = []
    hasPath = False
    # @param root, a tree node
    # @param sum, an integer
    # @return a boolean
    def hasPathSum(self, root, sum):
        self.sum = sum
        self.mapTree(root)

        return self.hasPath

    def mapTree(self, node):
        if node is None:
            return None
        self.arr.append(node.val)
        if node.left is not None:
            self.mapTree(node.left)
        if node.right is not None:
            self.mapTree(node.right)
        if node.left is None and node.right is None:
            pathsum = 0
            for val in self.arr:
                pathsum = pathsum + val
            if pathsum == self.sum:
                self.hasPath = True    
        self.arr.pop()

su = Solution()

n = TreeNode(0)

root = n

i = 1

while i < 10:
    n.left = TreeNode(i)
    n = n.left
    i += 1

next = root

print su.hasPathSum(root, 0)