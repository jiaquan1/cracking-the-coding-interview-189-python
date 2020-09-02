# read 500MB content each time, do merge sort, and write it back to the file.  And then merge 40 sorted lists
def mergesort(arr):
    if len(arr)==1:
        return arr
    if len(arr)>1:
        mid = len(arr)//2
    L = arr[:mid]
    R = arr[mid:]
    mergesort(L)
    mergesort(R)
    i=j=k = 0
    while i<len(L) and j<len(R):
        if L[i]<R[j]:
            arr[k]=L[i]
            i+=1
        else:
            arr[k]=R[j]
            j+=1
        k+=1
    while i<len(L):
        arr[k]=L[i]
        i+=1
        k+=1
    while j<len(R):
        arr[k]=R[j]
        j+=1
        k+=1
    return arr
#leetcode 21 and 23
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def mergeKLists(self, lists):
        if not lists:
            return None
        if len(lists) == 1:
            return lists[0]
        start, end = 0, len(lists)
        mid = start + (end - start) // 2
        left = self.mergeKLists(lists[:mid])
        right = self.mergeKLists(lists[mid:])
        return self.mergeTwoLists(left, right)
        
    
    def mergeTwoLists(self, L1, L2):
        head = cur = ListNode()
        while L1 and L2:
            if L1.val < L2.val:
                cur.next = L1
                L1 = L1.next
            else:
                cur.next = L2
                L2 = L2.next
            cur = cur.next
        cur.next = L1 or L2
        return head.next
    
    

import unittest
class Test(unittest.TestCase):
    def test(self):
        arr= [12,11,13,5,6,7]
        self.assertEqual(mergesort(arr),[5,6,7,11,12,13])
        pass
 
if __name__ =="__main__":
    unittest.main()
    
    

        
