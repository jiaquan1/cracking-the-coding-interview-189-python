

def powersets(set0):
    ps = {frozenset()}
    for element in set0:
        additions = set()
        for subset in ps:
            additions.add(subset.union(element))
        ps = ps.union(additions)
    return ps



import unittest

class Test(unittest.TestCase):
  def test(self):
    s = {'a', 'b', 'c', 'd'}
    ps = powersets(s)
    self.assertEqual(len(ps), 16)
    subsets = [set(), {'a'}, {'b'}, {'c'}, {'d'},
        {'a', 'b'}, {'a', 'c'}, {'a', 'd'}, {'b', 'c'}, {'b', 'd'}, {'c', 'd'},
        {'a', 'b', 'c'}, {'a', 'b', 'd'}, {'a', 'c', 'd'}, {'b', 'c', 'd'}, s]
    self.assertEqual(ps, set([frozenset(s) for s in subsets]))
    

if __name__ == "__main__":
  unittest.main()
        
        