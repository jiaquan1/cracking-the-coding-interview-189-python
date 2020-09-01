#leetcode 98
class Node():
    def __init__(self,data=None,left=None,right=None):
        self.data = data
        self.left = left
        self.right = right
class Solution():
    def __init__(self):
        self.last = float('-inf')
    def isValidBST(self,root):
        if not root:
            return True
        if not self.isValidBST(root.left):
            return False
        if self.last !=float('-inf') and root.data<=self.last:
            return False
        self.last = root.data
        if not self.isValidBST(root.right):
            return False
        return True
def isvalidbst2(root):
    if not root:
        return True
    stack = [(root, float('-inf'),float('inf'))]
    while stack:
        node, lower, upper = stack.pop()
        if not node:
            continue
        val = node.data
        #print(lower, val, upper)
        if val <=lower or val >=upper:
            
            return False
        stack.append((node.right,val,upper))
        stack.append((node.left,lower,val))
    return True

import unittest
class Test(unittest.TestCase):
    def test(self):
        root1 = Node(2,Node(1),Node(3))
        root2 = Node(1,Node(1))
        root3 = Node(5,Node(1),Node(4,Node(3),Node(6)))
        a= Solution()
        self.assertEqual(a.isValidBST(root1),True)
        self.assertEqual(a.isValidBST(root2),False)
        self.assertEqual(a.isValidBST(root3),False)
        self.assertEqual(isvalidbst2(root1),True)
        self.assertEqual(isvalidbst2(root2),False)
        self.assertEqual(isvalidbst2(root3),False)

if __name__=="__main__":
    unittest.main()