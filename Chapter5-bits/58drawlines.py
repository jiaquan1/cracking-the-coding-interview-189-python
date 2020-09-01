def drawlines(screen,width,x1,x2,y):
    byte_width = width//8
    height = len(screen)//byte_width
    if x1>x2:
        x1,x2 = x2,x1
    byte = y*byte_width+x1//8
    byte_end = y*byte_width+x2//8
    screen[byte] = (1<<(x1%8))-1
    byte +=1
    
    while byte<byte_end:
        screen[byte]= 255
        byte += 1
    screen[byte] = 255 ^((1<<(x2%8))-1)

import unittest

class Test(unittest.TestCase):
  def test_swap_odd_even_bits(self):
    screen = [0, 0, 0, 0, 0, 0, 0, 0,
              0, 0, 0, 0, 0, 0, 0, 0,
              0, 0, 0, 0, 0, 0, 0, 0]
    drawlines(screen, 64, 20, 42, 1)
    self.assertEqual(screen, [0]*8 + [0, 0, 15, 255, 255, 252, 0, 0] + [0]*8)
    


if __name__ == "__main__":
  unittest.main()

