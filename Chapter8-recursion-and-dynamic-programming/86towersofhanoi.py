

def towers_of_hanoi(tower1,tower2,tower3, n =None):
    if n == None:
        n = len(tower1.disc)
    if n ==0:
        return 
    towers_of_hanoi(tower1,tower3,tower2,n-1)
    disc= tower1.disc.pop()
    tower3.disc.append(disc)
    towers_of_hanoi(tower2,tower1,tower3,n-1)
class Tower(object):
    def __init__(self,name,disc= None):
        self.name = name
        if disc:
            self.disc = disc
        else:
            self.disc = []
    def __str__(self):
        return self.name


import unittest

class Test(unittest.TestCase):
  def test(self):
      tower1 = Tower('Tower1',["6", "5", "4", "3", "2", "1"])
      tower2 = Tower('Tower2',[])
      tower3 = Tower('Tower3',[])
      towers_of_hanoi(tower1,tower2,tower3)
      self.assertEqual(tower1.disc,[])
      self.assertEqual(tower2.disc,[])
      self.assertEqual(tower3.disc,["6", "5", "4", "3", "2", "1"] )
    

if __name__ == "__main__":
  unittest.main()
        
        