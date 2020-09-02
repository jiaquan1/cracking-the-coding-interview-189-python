
def sparse_search(array,target,leftix=0,rightix=None):
    if rightix == None:
        rightix = len(array)-1
    if leftix> rightix:
        return None
    middleix = (leftix+rightix)//2
    middle = array[middleix]
    if not middle:
        left = middleix-1
        right = middleix+1
        while True:
            if left<leftix or right>rightix:
                return None
            elif right<= rightix and array[right]:
                middleix = right
                break
            elif left>=leftix and array[left]:
                middleix = left
                break
            right+=1
            left-=1
    middle = array[middleix]
    # print(middleix,middle, rightix)
    if middle==target:
        return middleix
    elif middle > target:
        return sparse_search(array,target,leftix,middleix-1)
    else:
        return sparse_search(array,target,middleix+1,rightix)

import unittest
class Test(unittest.TestCase):
    def test(self):
        array = [0, 0, 7, 0, 0, 0, 0, 0, 19, 0, 0, 0, 0, 37, 40, 0, 0, 0]        
        self.assertEqual(sparse_search(array, 0), None)
        self.assertEqual(sparse_search(array, 7), 2)
        self.assertEqual(sparse_search(array, 19), 8)
        self.assertEqual(sparse_search(array, 37), 13)
        self.assertEqual(sparse_search(array, 40), 14)
        array = [0, 12, 0, 18, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
        self.assertEqual(sparse_search(array, 12), 1)
        self.assertEqual(sparse_search(array, 18), 3)
        pass
if __name__ =="__main__":
    unittest.main()
    
    

        
