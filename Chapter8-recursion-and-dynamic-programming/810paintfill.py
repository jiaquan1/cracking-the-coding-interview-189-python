
#leetcode 22
def paint_fill(image,c,r,color):
    if r<0 or c<0 or r>=len(image) or c>=len(image[r]):
        return 
    old_color = image[r][c]
    if old_color==color:
        return
    paintfillcolor(image,c,r,old_color,color)
def paintfillcolor(image,c,r,old_color,color):
    if image[r][c]!=old_color:
        return
    image[r][c]=color
    if r>0:
        paintfillcolor(image,c,r-1,old_color,color)
    if r<len(image)-1:
        paintfillcolor(image,c,r+1,old_color,color)
    if c>0:
        paintfillcolor(image,c-1,r,old_color,color)
    if c<len(image[r])-1:
        paintfillcolor(image,c+1,r,old_color,color)
    




import unittest

class Test(unittest.TestCase):
    def test(self):
        image1 = [[10, 10, 10, 10, 10, 10, 10, 40],
              [30, 20, 20, 10, 10, 40, 40, 40],
              [10, 10, 20, 20, 10, 10, 10, 10],
              [10, 10, 30, 20, 20, 20, 20, 10],
              [40, 40, 10, 10, 10, 10, 10, 10]]
        image2 = [[30, 30, 30, 30, 30, 30, 30, 40],
              [30, 20, 20, 30, 30, 40, 40, 40],
              [10, 10, 20, 20, 30, 30, 30, 30],
              [10, 10, 30, 20, 20, 20, 20, 30],
              [40, 40, 30, 30, 30, 30, 30, 30]]
        image3 = [[30, 30, 30, 30, 30, 30, 30, 40],
              [30, 20, 20, 30, 30, 40, 40, 40],
              [30, 30, 20, 20, 30, 30, 30, 30],
              [30, 30, 30, 20, 20, 20, 20, 30],
              [40, 40, 30, 30, 30, 30, 30, 30]]
        paint_fill(image1, 3, 1, 30)
        self.assertEqual(image1, image2)
        paint_fill(image1, 3, 1, 10)
        paint_fill(image1, 3, 1, 30)
        self.assertEqual(image1, image3)
      
if __name__ == "__main__":
  unittest.main()
        
        