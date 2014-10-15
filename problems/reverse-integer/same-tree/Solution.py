# Definition for a  binary tree node
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    # @param p, a tree node
    # @param q, a tree node
    # @return a boolean
    def isSameTree(self, p, q):
        if p is None and q is None:
            return True
        else:
            if p is None or q is None:
                return False
            if p.val == q.val:
                left = None
                right = None
                left = self.isSameTree(p.left, q.left)
                right = self.isSameTree(p.right, q.right)
                if left is True and right is True:
                    return True
                else:
                    return False
            else:
                return False
        

su = Solution()

n1 = TreeNode(1)
n1.left = None

n2 = TreeNode(1)
n2.left = None
# n2.right = TreeNode(2)

print su.isSameTree(n1, n2)

