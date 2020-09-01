#leetcode 70
import collections
def triple_step(n):
    
    if n<0:
        return 0
    if n==0:
        return 1
    else:
        memo = collections.defaultdict()
        memo[-1]=0
        memo[0]=1
        memo[1]=1
    
    def helper(n):
        if n in memo:
            return memo[n]
        memo[n]= helper(n-1)+helper(n-2)+helper(n-3)
        return memo[n]    
    helper(n)
    return memo[n]

import unittest

class Test(unittest.TestCase):
  def test_triple_step(self):
    self.assertEqual(triple_step(3), 4)
    self.assertEqual(triple_step(7), 44)

if __name__ == "__main__":
  unittest.main()
        
        