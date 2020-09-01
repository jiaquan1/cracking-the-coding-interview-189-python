
#leetcode 22
def parens(n):
    left = right = n
    res = []
    path = ""
    def dfs(left,right,path):
        if left ==0 and right ==0:
            res.append(path)
            return
        else:
            if left>right:
                return
            if left:
                dfs(left-1,right,path + "(")
            if right:
                dfs(left,right-1,path +")")
    dfs(left,right,path)
    return res



import unittest

class Test(unittest.TestCase):
  def test(self):
      self.assertEqual(parens(1),['()'])
      self.assertEqual(parens(2),['(())','()()'])
    
      
    

if __name__ == "__main__":
  unittest.main()
        
        