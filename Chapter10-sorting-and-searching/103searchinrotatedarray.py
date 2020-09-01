
#leetcode 33 and leetcode 81
def rotated_search(array, target,leftix= 0, rightix = None):
    if rightix == None:
        rightix = len(array)
    if rightix<=leftix:
        return None
    middleix = (leftix + rightix)//2
    left = array[leftix]
    middle = array[middleix]
    if target == middle:
        return middleix
    if target == left:
        return leftix
    if left > middle:
        if middle<target<left:
            return rotated_search(array,target,middleix+1,rightix)
        else:
            return rotated_search(array,target,leftix+1,middleix)
    elif left<target<middle:
        return rotated_search(array,target,leftix+1,middleix)
    else:
        return rotated_search(array,target,middleix+1,rightix)

import unittest
class Test(unittest.TestCase):
    def test(self):
        array = [55, 60, 65, 70, 75, 80, 85, 90, 95, 15, 20, 25, 30, 35, 40, 45]
        self.assertEqual(rotated_search(array, 55), 0)
        self.assertEqual(rotated_search(array, 60), 1)
        self.assertEqual(rotated_search(array, 90), 7)
        self.assertEqual(rotated_search(array, 95), 8)
        self.assertEqual(rotated_search(array, 15), 9)
        self.assertEqual(rotated_search(array, 30), 12)
        self.assertEqual(rotated_search(array, 45), 15)

if __name__ =="__main__":
    unittest.main()
    
    

        
