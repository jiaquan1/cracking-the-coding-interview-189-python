def checksubtree(t1,t2):
    for node in tree_generator(t1):
        if equivalenttree(node,t2):
            return True
    return False
def equivalenttree(t1,t2):
    if not t1 and not t2:
        return True
    elif not t1 or not t2:
        return False
    elif t1.data!=t2.data:
        return False
    else:
        return equivalenttree(t1.left, t2.left) and equivalenttree(t1.right,t2.right)    
def tree_generator(t1):
    if not t1:
        return 
    yield t1
    for child in tree_generator(t1.left):
        yield child
    for child in tree_generator(t1.right):
        yield child

def checksubtree2(t1,t2):
    if not t1 and not t2:
        return True
    elif not t1 or not t2:
        return False
    string1= []
    string2= []
    string1 = getstring(t1,string1)
    string2 = getstring(t2,string2)
    for i in range(len(string1)):
        if string1[i:i+len(string2)]==string2:
            return True
    return False
def getstring(node,path):
    if not node:
        path.append('X')
        return
    path.append(str(node.data) + ' ')
    getstring(node.left,path)
    getstring(node.right,path)
    return path

class Node():
    def __init__(self,data=None,left= None,right= None):
        self.data,self.left,self.right = data,left,right

import unittest

class Test(unittest.TestCase):
  def test_is_subtree(self):
    tree1 = Node(5,Node(3,Node(2),Node(4)),Node(8,Node(7,Node(9)),Node(1)))
    tree2 = Node(8,Node(7),Node(1))
    self.assertEqual(checksubtree(tree1, tree2), False)
    self.assertEqual(checksubtree2(tree1, tree2), False)
    tree3 = Node(8,Node(7,Node(9)),Node(1))
    self.assertEqual(checksubtree(tree1, tree3), True)
    self.assertEqual(checksubtree2(tree1, tree3), True)

if __name__ == "__main__":
  unittest.main()
    