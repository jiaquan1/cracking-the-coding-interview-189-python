#leetcode 285 (no link to parent) and 510(link to parent)
class Node():
    def __init__(self,data=None,left=None,right=None):
        self.val = data
        self.left = left
        self.right = right
def successor(root,p):
    if not root:
        return None
    suc = None
    while root:
        if root.val>p.val:
            suc = root
            root= root.left
        else:
            root = root.right
    return suc

import unittest
class Test(unittest.TestCase):
    def test(self):
        root1 = Node(5,Node(1),Node(8,Node(6),Node(9)))
        p1 = Node(1)
        p2 = Node(8)
        self.assertEqual(successor(root1,p1).val,5)
        self.assertEqual(successor(root1,p2).val,9)
if __name__=='__main__':
    unittest.main()




