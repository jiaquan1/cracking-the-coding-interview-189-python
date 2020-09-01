

def magicindex(array):
    if len(array) == 0 or array[0] > 0 or array[-1] < len(array) - 1:
        return None
    return magicfast(array, 0 ,len(array)-1)
def magicfast(array,start,end):
    if end < start:
        return
    mid = (start+end)//2
    if array[mid]==mid:
        return mid
    elif array[mid]>mid:
        return magicfast(array,start,mid-1)
    elif array[mid]<mid:
        return magicfast(array,mid+1,end)
def magicindex2(array):
    if len(array)==0:
        return None
    return magicfast2(array,0,len(array)-1)
def magicfast2(array,start,end):
    if end<start:
        return
    mid = (start+end)//2
    if array[mid]==mid:
        return mid
    leftindex = min(mid-1,array[mid])
    left = magicfast2(array,start,leftindex)
    if left and left>=0:
        return left
    rightindex = max(mid+1,array[mid])
    right = magicfast2(array,rightindex,end)
    return right



import unittest

class Test(unittest.TestCase):
  def test(self):
    self.assertEqual(magicindex([3,4,5]),None)
    self.assertEqual(magicindex([-2,-1,0,2]),None)
    self.assertEqual(magicindex([-20,0,1,2,3,4,5,7,20]), 7)
    self.assertEqual(magicindex([-20,1,2,3,4,5,6,20]), 3)
    self.assertEqual(magicindex2([2,2,2,2,2,2,2,3,4]),2)
    self.assertEqual(magicindex2([1,2,3,5,5,5,5,5,5,5,5,10,11]),5)

if __name__ == "__main__":
  unittest.main()
        
        