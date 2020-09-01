

def recursivemultiply(a,b):
    small = min(a,b)
    big = max(a,b)
    memo = {}
    return helper(small,big,memo)
def helper(small,big,memo):
    if small ==0:
        return 0
    elif small == 1:
        return big
    else:
        s = small>>1
        half = helper(s,big,memo)
        if small%2:
            memo[small]=half+half+big
        else:
            memo[small]=half+half
        return memo[small]


import unittest

class Test(unittest.TestCase):
  def test(self):
    
    self.assertEqual(recursivemultiply(8,7),56)
    

if __name__ == "__main__":
  unittest.main()
        
        