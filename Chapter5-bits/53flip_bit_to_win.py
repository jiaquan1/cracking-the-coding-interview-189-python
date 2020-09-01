<<<<<<< HEAD
def flip_bit(bits):
    bit = 1<<63
    maxlen = 0
    cur_without_flip = 0
    cur_with_flip = 0
    while bit:
        if bits&bit:
            cur_with_flip+=1
            cur_without_flip+=1
        else:
            cur_with_flip=cur_without_flip+1
            cur_without_flip=0
        if cur_with_flip>maxlen:
            maxlen=cur_with_flip
        bit>>=1
    return maxlen
    
import unittest
class Test(unittest.TestCase):
  def test_longest_sequence_after_flip(self):
    self.assertEqual(flip_bit(0b1111100), 6)
    self.assertEqual(flip_bit(0b0111111), 7)
    self.assertEqual(flip_bit(-1), 64)
    self.assertEqual(flip_bit(0b1011110111001111110), 8)

if __name__ == "__main__":
  unittest.main()
=======
def flip_bit(bits):
    bit = 1<<63
    maxlen = 0
    cur_without_flip = 0
    cur_with_flip = 0
    while bit:
        if bits&bit:
            cur_with_flip+=1
            cur_without_flip+=1
        else:
            cur_with_flip=cur_without_flip+1
            cur_without_flip=0
        if cur_with_flip>maxlen:
            maxlen=cur_with_flip
        bit>>=1
    return maxlen
    
import unittest
class Test(unittest.TestCase):
  def test_longest_sequence_after_flip(self):
    self.assertEqual(flip_bit(0b1111100), 6)
    self.assertEqual(flip_bit(0b0111111), 7)
    self.assertEqual(flip_bit(-1), 64)
    self.assertEqual(flip_bit(0b1011110111001111110), 8)

if __name__ == "__main__":
  unittest.main()
>>>>>>> 45e00abd356375b5fb384fa23f21f34195b99a48
    