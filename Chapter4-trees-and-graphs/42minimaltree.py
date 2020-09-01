class Node():
    def __init__(self,data=None,left=None,right=None):
        self.data = data
        self.left = left
        self.right = right

def minimaltree(sortedarray):
    if not sortedarray:
        return None
    mid = len(sortedarray)//2
    root = Node(sortedarray[mid])
    root.left = minimaltree(sortedarray[:mid])
    root.right = minimaltree(sortedarray[mid+1:])
    return root

import unittest
class Test(unittest.TestCase):
    def test(self):
        sortedarray=[1,2,3]
        root = minimaltree(sortedarray)
        self.assertEqual((root.data, root.left.data,root.right.data),(2,1,3))
if __name__=="__main__":
    unittest.main()

