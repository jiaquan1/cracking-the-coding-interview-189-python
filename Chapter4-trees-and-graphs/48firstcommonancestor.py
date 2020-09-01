#leetcode 235(BST) and 236(BT)
class Node():
    def __init__(self,data=None,left=None,right=None):
        self.val = data
        self.left = left
        self.right = right
def firstcommonancestor(root,p,q):
    if not root:
        return None
    if root.val == p.val or root.val==q.val:
        return root
    left = right = None
    left = firstcommonancestor(root.left,p,q)
    right = firstcommonancestor(root.right,p,q)
    if left and right:
        return root
    else:
        return left or right

root1 = Node(5,Node(1),Node(8,Node(6),Node(9)))
p = Node(1)
q1 = Node(8)
q2 = Node(5)
print(firstcommonancestor(root1,p,q1).val, firstcommonancestor(root1,p,q2).val )

