<<<<<<< HEAD
def bits_different_1(a,b):
    c = a^b
    count = 0
    while c !=0:
        count += c&1
        c>>=1
    return count
def bits_different_2(a,b):
    c = a^b
    count = 0
    while c !=0:
        count +=1
        c = c&(c-1)
    return count


import unittest

class Test(unittest.TestCase):
    def test(self):
        self.assertEqual(bits_different_1(16, 2), 2)
        self.assertEqual(bits_different_1(17, 34), 4)
        self.assertEqual(bits_different_1(15, 97), 5)
        self.assertEqual(bits_different_2(16, 2), 2)
        self.assertEqual(bits_different_2(17, 34), 4)
        self.assertEqual(bits_different_2(15, 97), 5)
    


if __name__ == "__main__":
  unittest.main()

=======
def bits_different_1(a,b):
    c = a^b
    count = 0
    while c !=0:
        count += c&1
        c>>=1
    return count
def bits_different_2(a,b):
    c = a^b
    count = 0
    while c !=0:
        count +=1
        c = c&(c-1)
    return count


import unittest

class Test(unittest.TestCase):
    def test(self):
        self.assertEqual(bits_different_1(16, 2), 2)
        self.assertEqual(bits_different_1(17, 34), 4)
        self.assertEqual(bits_different_1(15, 97), 5)
        self.assertEqual(bits_different_2(16, 2), 2)
        self.assertEqual(bits_different_2(17, 34), 4)
        self.assertEqual(bits_different_2(15, 97), 5)
    


if __name__ == "__main__":
  unittest.main()

>>>>>>> 45e00abd356375b5fb384fa23f21f34195b99a48
