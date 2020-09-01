

def permutationwithdup(string):
    return partial_permutation("",sorted(string))
def partial_permutation(partial,string_left):
    if len(string_left)==0:
        return [partial]
    permutation = []
    previousletter = None
    for i, letter in enumerate(string_left):
        if letter==previousletter:
            continue
        nextleft = string_left[:i]+string_left[i+1:]
        permutation += partial_permutation(partial + letter, nextleft)
        previousletter = letter
    return permutation



import unittest

class Test(unittest.TestCase):
  def test(self):
    self.assertEqual(permutationwithdup("ABCD"), ["ABCD", "ABDC", "ACBD", "ACDB",
        "ADBC", "ADCB", "BACD", "BADC", "BCAD", "BCDA", "BDAC", "BDCA",
        "CABD", "CADB", "CBAD", "CBDA", "CDAB", "CDBA", "DABC", "DACB",
        "DBAC", "DBCA", "DCAB", "DCBA"])
    self.assertEqual(permutationwithdup("abca"), ["aabc", "aacb", "abac", "abca","acab", "acba", "baac", "baca", "bcaa", "caab", "caba", "cbaa"])
      
    

if __name__ == "__main__":
  unittest.main()
        
        