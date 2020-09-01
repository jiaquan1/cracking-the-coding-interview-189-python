
#leetcode 51
def nqueens(n):
    def dfs(queens,xy_dif,xy_sum):
        p = len(queens)
        if p==n:
            res.append(queens)
        for q in range(n):
            if q not in queens and p-q not in xy_dif and p+q not in xy_sum:
                dfs(queens+[q],xy_dif+[p-q],xy_sum+[p+q])
    res = []
    dfs([],[],[])
    return [["."*i + "Q" + "."*(n-i-1) for i in sol] for sol in res]


import unittest

class Test(unittest.TestCase):
    def test(self):
        n = 4
        Output= [
        [".Q..",  
        "...Q",
        "Q...",
        "..Q."],

        ["..Q.",  
        "Q...",
        "...Q",
        ".Q.."]
        ]
        self.assertEqual(nqueens(n),Output)
        
if __name__ == "__main__":
  unittest.main()
        
        