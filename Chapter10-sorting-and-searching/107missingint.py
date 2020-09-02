# 4 billion bits in file filename, scanner to get each value from filename, bit vector to store the value, here I assume the scanner function, no way to test 
def missingint(filename):
    numberofints = len(filename)
    in = scanner(filename)
    bitfield = [0]*numberofints
    while in.hasNextInt():
        n = in.NextInt
        bitfield[n//8] = bitfiled[n//8]|(1<<(n%8))
    for i in range(numberofints):
        for j in range(8):
            if ((bitfield[i]&(1<<j))==0):
                return i*8+j

    

    

import unittest
class Test(unittest.TestCase):
    def test(self):
        
        pass
 
if __name__ =="__main__":
    unittest.main()
    
    

        
