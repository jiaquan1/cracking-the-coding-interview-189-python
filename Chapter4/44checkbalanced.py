#leetcode 110
class Node():
    def __init__(self,data=None,left=None,right=None):
        self.data = data
        self.left = left
        self.right = right

def isbalanced(root):
    if not root:
        return True
    heightdiff = getheight(root.left)-getheight(root.right)
    if abs(heightdiff)>1:
        return False
    else:
        return isbalanced(root.left) and isbalanced(root.right)
def getheight(root):
    if not root:
        return 0
    return max(getheight(root.left),getheight(root.right))+1
def getheight2(root):
    if not root:
        return 0
    left = getheight2(root.left)
    if left == float('-inf'):
        return float('-inf')
    right = getheight2(root.right)
    if right == float('-inf'):
        return float('-inf')
    heightdiff2 = abs(left-right)
    if heightdiff2>1:
        return float('-inf')
    return max(left,right)+1
def isbalanced2(root):
    if not root:
        return True
    return getheight2(root)!=float('-inf')

import unittest
class Test(unittest.TestCase):
    def test(self):

        tree1 = Node(3,Node(1),Node(2))
        tree2 = Node(3,Node(1,Node(4,Node(6)),Node(5)),Node(2))
        self.assertEqual(isbalanced(tree1),True)
        self.assertEqual(isbalanced(tree2), False)
        self.assertEqual(isbalanced2(tree1),True)
        self.assertEqual(isbalanced2(tree2), False)
if __name__=="__main__":
    unittest.main()
    