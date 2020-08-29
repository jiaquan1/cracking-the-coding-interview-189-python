class Node():
    def __init__(self,data=None,left=None,right=None):
        self.data = data
        self.left = left
        self.right = right

class ListNode():
    def __init__(self,data=None,next=None):
        self.data = data
        self.next = next

import collections
def listofdepth(root):
    if not root:
        return None
    q = collections.deque()
    q.append(root)
    lists = []
    level = 0
    while q:    
        node = q.popleft()
        head=newlist = ListNode(node.data)
        newq = collections.deque()
        if node.left:
                newq.append(node.left)
        if node.right:
            newq.append(node.right)
        while q:
            node = q.popleft()
            newlist.next = ListNode(node.data)
            newlist = newlist.next
            if node.left:
                newq.append(node.left)
            if node.right:
                newq.append(node.right)
            
        lists.append(head)
        level += 1
        q = newq
    return lists
import unittest
class Test(unittest.TestCase):
    def test(self):
        root = Node(3,Node(1,Node(4),Node(5)),Node(2))
        res = []
        for list in listofdepth(root):
            res.append([])
            while list:
                res[-1].append(list.data)
                list = list.next
        self.assertEqual(res,[[3],[1,2],[4,5]])

if __name__=="__main__":
    unittest.main()

    

    

