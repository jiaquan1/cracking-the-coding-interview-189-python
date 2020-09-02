# leetcode 329 and 240
def searchmatrix(matrix,target):
    if not matrix:
        return False
    def search_rec(left,up,right,down):
        if left>right or up>down:
            return False
        elif target<matrix[up][left] or target>matrix[down][right]:
            return False
        mid = left +(right - left)//2
        row = up
        while row<=down and matrix[row][mid]<=target:
            if matrix[row][mid]==target:
                return True
            row += 1
        return search_rec(left,row,mid-1,down) or search_rec(mid+1,up,right,row-1)
    return search_rec(0,0,len(matrix[0])-1,len(matrix)-1)

import unittest
class Test(unittest.TestCase):
    def test(self):
        array = [
        [1,   4,  7, 11, 15],
        [2,   5,  8, 12, 19],
        [3,   6,  9, 16, 22],
        [10, 13, 14, 17, 24],
        [18, 21, 23, 26, 30]
        ]
        self.assertEqual(searchmatrix(array,5),True)
        self.assertEqual(searchmatrix(array,20),False)
        
        pass
 
if __name__ =="__main__":
    unittest.main()
    
    

        
