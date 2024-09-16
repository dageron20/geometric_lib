class CircleTestCase(unittest.TestCase):

 def test_circle_area(self):
     c_area = area(10)
     self.assertAlmostEqual(c_area, 314.2, delta=0.1)
     self.assertIsInstance(c_area, float)

     with self.assertRaises(ValueError):
         area(-10)

 def test_circle_perimeter(self):
     c_peri = perimeter(10)
     self.assertAlmostEqual(c_peri, 62.8, delta=0.1)
     self.assertIsInstance(c_peri, float)

     with self.assertRaises(ValueError):
         perimeter(-10)
