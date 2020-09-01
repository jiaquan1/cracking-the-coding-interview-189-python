class Node():
    def __init__(self, data= None, left = None, right = None):
        self.data = data
        self.left = left
        self.right = right
        self.count = 1
        if self.left:
            self.count += self.left.count
        if self.right:
            self.count += self.right.count
    def getrandomnode(self):
        return self.getnumberednode(randint(0,self.count-1))
    def getnumberednode(self,number):
        if number ==0:
            return self
        if self.left:
            if number -1 < self.left.count:
                return self.left.getnumberednode(number -1)
            elif self.right:
                return self.right.getnumberednode(number-1-self.left.count)
        if self.right:
            return self.right.getnumberednode(number-1)
        return None

import random
import unittest
def randint(lower, upper):
    if not mock is False:
        return mock
    return random.randint(lower, upper)

class Test(unittest.TestCase):
    def test_mock_randint(self):
        global mock
        mock = 12
        self.assertEqual(randint(0, 2000), 12)
  
    def test_get_random_value(self):
        global mock
        tree = Node(11,Node(21,Node(31),Node(32,Node(41),Node(42,None,Node(51)))),
                    Node(22,Node(33),Node(34)))
        mock = 0
        self.assertEqual(tree.getrandomnode().data, 11)
        mock = 4
        self.assertEqual(tree.getrandomnode().data, 41)
        mock = 8
        self.assertEqual(tree.getrandomnode().data, 33)

if __name__ == "__main__":
  unittest.main()