class RectangleTestCase(unittest.TestCase):
 
 def test_zero_mul(self):
   res = area(10, 0)
   self.assertEqual(res, 0)
   self.assertIsInstance(res, int)
   with self.assertRaises(ValueError):
       area(-10, 0)

 def test_square_mul(self):
    res = area(10, 10)
    self.assertEqual(res, 100)
    self.assertIsInstance(res, int)
    with self.assertRaises(ValueError):
        area(10, -10)

 def test_zero_perimeter(self):
   res = perimeter(0, 0)
   self.assertEqual(res, 0)
   self.assertIsInstance(res, int)
   with self.assertRaises(ValueError):
       perimeter(-10, 0)

 def test_square_perimeter(self):
    res = perimeter(10, 10)
    self.assertEqual(res, 40)
    self.assertIsInstance(res, int)
    with self.assertRaises(ValueError):
        perimeter(10, -10)


