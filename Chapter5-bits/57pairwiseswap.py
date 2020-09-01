<<<<<<< HEAD
EVEN = 0x5555555555555555
ODD  = 0xAAAAAAAAAAAAAAAA

def swap_odd_even_bits(n):
  return ((n & ODD) >> 1) | ((n & EVEN) << 1)

import unittest

class Test(unittest.TestCase):
  def test_swap_odd_even_bits(self):
    self.assertEqual(swap_odd_even_bits(42), 21)
    self.assertEqual(swap_odd_even_bits(21), 42)
    self.assertEqual(swap_odd_even_bits(43), 23)
    self.assertEqual(swap_odd_even_bits(EVEN), ODD)
    self.assertEqual(swap_odd_even_bits(511), 767)
    self.assertEqual(swap_odd_even_bits(1023), 1023)
    


if __name__ == "__main__":
  unittest.main()

=======
EVEN = 0x5555555555555555
ODD  = 0xAAAAAAAAAAAAAAAA

def swap_odd_even_bits(n):
  return ((n & ODD) >> 1) | ((n & EVEN) << 1)

import unittest

class Test(unittest.TestCase):
  def test_swap_odd_even_bits(self):
    self.assertEqual(swap_odd_even_bits(42), 21)
    self.assertEqual(swap_odd_even_bits(21), 42)
    self.assertEqual(swap_odd_even_bits(43), 23)
    self.assertEqual(swap_odd_even_bits(EVEN), ODD)
    self.assertEqual(swap_odd_even_bits(511), 767)
    self.assertEqual(swap_odd_even_bits(1023), 1023)
    


if __name__ == "__main__":
  unittest.main()

>>>>>>> 45e00abd356375b5fb384fa23f21f34195b99a48
