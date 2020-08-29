def bst_sequences(bst):
    return helper([],[bst])

def helper(path, subtrees):
    if not len(subtrees):
        return [path]
    sequences = []
    for index, subtree in enumerate(subtrees):
        nextpath = path + [subtree.data]
        nextsubtrees = subtrees[:index]+subtrees[index+1:]
        if subtree.left:
            nextsubtrees.append(subtree.left)
        if subtree.right:
            nextsubtrees.append(subtree.right)
        sequences += helper(nextpath,nextsubtrees)
    return sequences

class Node():
    def __init__(self,data = None, left = None, right = None):
        self.data, self.left, self.right = data, left, right

import unittest

class Test(unittest.TestCase):
    def test_bst_sequences(self):
        self.assertEqual(bst_sequences(Node(7,Node(4,Node(5)),Node(9))), [[7, 4, 9, 5],[7, 4, 5, 9],[7, 9, 4, 5]])
        self.assertEqual(bst_sequences(Node(7,Node(4,Node(5),Node(6)),Node(9))), [
            [7, 4, 9, 5, 6],
            [7, 4, 9, 6, 5],
            [7, 4, 5, 9, 6],
            [7, 4, 5, 6, 9],
            [7, 4, 6, 9, 5],
            [7, 4, 6, 5, 9],
            [7, 9, 4, 5, 6],
            [7, 9, 4, 6, 5]])

if __name__ == "__main__":
  unittest.main()
