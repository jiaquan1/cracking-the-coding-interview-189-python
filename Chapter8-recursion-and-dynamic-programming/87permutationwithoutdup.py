

def permutationwithoutdup(string):
    return partial_permutation("",string)
def partial_permutation(partial,string_left):
    if len(string_left)==0:
        return [partial]
    permutation = []
    for i, letter in enumerate(string_left):
        nextleft = string_left[:i]+string_left[i+1:]
        permutation += partial_permutation(partial + letter, nextleft)
    return permutation



import unittest

class Test(unittest.TestCase):
  def test(self):
      self.assertEqual(permutationwithoutdup("ABCD"), ["ABCD", "ABDC", "ACBD", "ACDB",
        "ADBC", "ADCB", "BACD", "BADC", "BCAD", "BCDA", "BDAC", "BDCA",
        "CABD", "CADB", "CBAD", "CBDA", "CDAB", "CDBA", "DABC", "DACB",
        "DBAC", "DBCA", "DCAB", "DCBA"])
      
    

if __name__ == "__main__":
  unittest.main()
        
        