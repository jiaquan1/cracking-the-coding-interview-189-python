<<<<<<< HEAD
def next_numbers(number):
    if number <=0:
        return None,None
    if number%2:
        a = 1
        c1=0
        #large
        while number&a and number>=a:
            c1+=1
            a<<=1
        
        if number<a:
            large = a+(1<<(c1-1))-1
        else:
            large = ((number//a+1)<<c1) + (1<<(c1-1))-1
        #small
        b = 1
        c0=0
        c00=0
        while number&b:
            b<<=1
            c0+=1
        if number<b:
            small = None
        else:
            while not number&b:
                b<<=1
                c00+=1
            print('b=',b,'c0=',c0,)
            small = ((number//b-1)*b)+(((1<<(c0+1))-1)<<(c00-1))

    else:
        #large
        a=1
        c1=0
        while not number&a:
            a<<=1
        while number&a and number>=a:
            c1+=1
            a<<=1
        if number<a:
            large = a+(1<<(c1-1))-1
        else:
            large = ((number//a+1)<<c1) + (1<<(c1-1))-1
        #small
        b=1 
        c0=0
        while not number&b:
            b<<=1
        small = ((number//b-1)*b)+(b>>1)


        
    return (small,large)
import unittest

class Test(unittest.TestCase):
  def test_next_numbers(self):
    self.assertEqual(next_numbers(8), (4, 16))
    self.assertEqual(next_numbers(12), (10, 17))
    self.assertEqual(next_numbers(15), (None, 23))
    self.assertEqual(next_numbers(143), (124, 151))
    self.assertEqual(next_numbers(159), (126, 175))

if __name__ == "__main__":
  unittest.main()

=======
def next_numbers(number):
    if number <=0:
        return None,None
    if number%2:
        a = 1
        c1=0
        #large
        while number&a and number>=a:
            c1+=1
            a<<=1
        
        if number<a:
            large = a+(1<<(c1-1))-1
        else:
            large = ((number//a+1)<<c1) + (1<<(c1-1))-1
        #small
        b = 1
        c0=0
        c00=0
        while number&b:
            b<<=1
            c0+=1
        if number<b:
            small = None
        else:
            while not number&b:
                b<<=1
                c00+=1
            print('b=',b,'c0=',c0,)
            small = ((number//b-1)*b)+(((1<<(c0+1))-1)<<(c00-1))

    else:
        #large
        a=1
        c1=0
        while not number&a:
            a<<=1
        while number&a and number>=a:
            c1+=1
            a<<=1
        if number<a:
            large = a+(1<<(c1-1))-1
        else:
            large = ((number//a+1)<<c1) + (1<<(c1-1))-1
        #small
        b=1 
        c0=0
        while not number&b:
            b<<=1
        small = ((number//b-1)*b)+(b>>1)


        
    return (small,large)
import unittest

class Test(unittest.TestCase):
  def test_next_numbers(self):
    self.assertEqual(next_numbers(8), (4, 16))
    self.assertEqual(next_numbers(12), (10, 17))
    self.assertEqual(next_numbers(15), (None, 23))
    self.assertEqual(next_numbers(143), (124, 151))
    self.assertEqual(next_numbers(159), (126, 175))

if __name__ == "__main__":
  unittest.main()

>>>>>>> 45e00abd356375b5fb384fa23f21f34195b99a48
