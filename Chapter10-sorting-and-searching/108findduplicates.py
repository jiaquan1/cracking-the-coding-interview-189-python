# 4 kilobytes memory is 8*4*2**10 = 2**15 bits, >32000, so one bit vector is enough
def findduplicates(array):
    bitvector = [0]*1024
    duplicates = []
    for n in array:
        bit = 1<<(n%32)
        if bitvector[n//32] & bit:
            duplicates.append(n)
        else:
            bitvector[n//32]=bitvector[n//32]|bit
    return duplicates

    

    

import unittest
class Test(unittest.TestCase):
    def test(self):
        array = [1, 2, 3, 4, 55, 20000, 20001, 20002, 20003, 17, 18, 19, 20, 22, 23,
             7, 2, 3, 3, 55, 20002, 20004, 20005, 20006, 16, 18, 22, 24, 25, 26]
        self.assertEqual(findduplicates(array), [2, 3, 3, 55, 20002, 18, 22])
        
        pass
 
if __name__ =="__main__":
    unittest.main()
    
    

        
