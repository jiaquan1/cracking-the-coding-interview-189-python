#leetcode 437
class Node():
    def __init__(self, data= None, left = None, right = None):
        self.val = data
        self.left = left
        self.right = right

def pathsum(root, targetsum):
    if not root:
        return 0
    return helper(root,targetsum) + pathsum(root.left, targetsum) + pathsum(root.right, targetsum)
def helper(root,target):
    if not root:
        return 0
    res = 0
    if root.val == target:
        res += 1
    left = helper(root.left, target - root.val)
    right = helper(root.right, target - root.val)
    return res + left + right

# leetcode 112
def pathsum1(root,target):
    if not root:
        return False
    if root and not root.left and not root.right and root.val == target:
        return True
    return pathsum1(root.left,target - root.val) or pathsum1(root.right, target - root.val)
#leetcode 113:
def pathsum2(root,target):
    if not root:
        return []
    res = []
    helper2(root,res,target,[])
    return res
def helper2(root,res,target,cur):
    if not root:
        return
    if not root.left and not root.right and root.val == target:
        cur.append(root.val)
        res.append(cur[:])
        cur.pop()
    if root.left:
        helper2(root.left,res,target-root.val, cur + [root.val])
    if root.right:
        helper2(root.right,res,target-root.val, cur + [root.val])
#leetcode 666
def pathsum4(nums):
    dictnode = collections.defaultdict(int)
    for num in nums:
        depth = num//100
        pos = (num//10)%10
        val = num%10
        dictnode[(depth,pos)] += dictnode[depth-1,(pos+1)//2]+val
    res = 0
    for depth,pos in dictnode.keys():
        if (depth+1, pos*2-1) and (depth+1, pos*2) not in dictnode:
            res += dictnode[(depth,pos)]
    return res

import collections
import unittest
class Test(unittest.TestCase):
    def test1(self):
        tree = Node(11,Node(21,Node(31),Node(32,Node(41),Node(42,None,Node(51)))),
                    Node(22,Node(33),Node(34)))
        tree2 = Node(5,Node(4,Node(11,Node(7),Node(2))),Node(8,Node(13),Node(4,Node(5),Node(1))))
       
        self.assertEqual(pathsum(tree, 11), 1)
        self.assertEqual(pathsum1(tree, 11), False)
        self.assertEqual(pathsum1(tree, 63), True)
        self.assertEqual(pathsum2(tree2,22),[[5,4,11,2],[5,8,4,5]])
        nums1 = [113,215,221]
        nums2 = [113,221]
        self.assertEqual(pathsum4(nums1),12)
        self.assertEqual(pathsum4(nums2),4)


if __name__ == "__main__":
  unittest.main()
