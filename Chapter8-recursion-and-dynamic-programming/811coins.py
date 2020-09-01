
#leetcode 518
def coins(n,coins):
    dp = [0 for _ in range(n+1)]
    dp[0]=1
    for coin in coins:
        for x in range(coin,n+1):
            dp[x] += dp[x-coin]
    return dp[n]
#leetcode 322
def coins2(n,coins):
    dp = [float('inf') for _ in range(n+1)]
    dp[0]=0
    for coin in coins:
        for x in range(coin,n+1):
            dp[x]=min(dp[x],dp[x-coin]+1)
    return dp[n] if dp[n]<float('inf') else -1

import unittest

class Test(unittest.TestCase):
    def test(self):
        self.assertEqual(coins(5,[1,2,5]),4)
        self.assertEqual(coins(3,[2]),0)
        self.assertEqual(coins2(11,[1,2,5]),3)
        self.assertEqual(coins2(3,[2]),-1)
    
      
if __name__ == "__main__":
  unittest.main()
        
        