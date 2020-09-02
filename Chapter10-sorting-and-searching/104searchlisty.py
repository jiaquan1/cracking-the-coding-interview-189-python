
def search_listy(listy, target,leftix= 0, rightix = None):
    if rightix == None:
        rightix = 2
    right = listy[rightix]
    while right <target and right !=-1:
        rightix *=2
        right = listy[rightix]
    if right==target:
        return rightix
    if leftix == rightix:
        return None
    middleix = (leftix+rightix)//2
    middle = listy[middleix]
    if middle==target:
        return middleix
    
    if middle==-1 or middle>target:
        return search_listy(listy,target,leftix,middleix)
    else:
        return search_listy(listy,target,middleix+1,rightix)

class Listy(object):
    def __init__(self,array):
        self.array = array
    def __getitem__(self,ix):
        if ix<len(self.array):
            return self.array[ix]
        return -1
    

import unittest
class Test(unittest.TestCase):
    def test(self):
        listy = Listy([-22, -11, 11, 22, 33, 44, 55, 66, 77, 88, 99])
        self.assertEqual(search_listy(listy, 25), None)
        self.assertEqual(search_listy(listy, -22), 0)
        self.assertEqual(search_listy(listy, 22), 3)
        self.assertEqual(search_listy(listy, 66), 7)
        self.assertEqual(search_listy(listy, 77), 8)
        self.assertEqual(search_listy(listy, 99), 10)
        self.assertEqual(search_listy(listy, 100), None)

if __name__ =="__main__":
    unittest.main()
    
    

        
