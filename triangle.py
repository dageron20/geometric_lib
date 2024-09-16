class TriangleTestCase(unittest.TestCase):

   def test_area(self):
       self.assertEqual(area(3, 4) , 6)
       self.assertIsInstance(area(3, 4), float)

   def test_perimeter(self):
       self.assertEqual(perimeter(3, 4, 5), 12)
       self.assertIsInstance(perimeter(3, 4, 5), int)

   def test_area_exception(self):
       with self.assertRaises(ValueError):
           area(-3, 4)

   def test_perimeter_exception(self):
       with self.assertRaises(ValueError):
           perimeter(-3, 4, 5)

