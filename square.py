class SquareTestCase(unittest.TestCase):

   def test_area(self):
       self.assertEqual(area(5), 25)
       self.assertEqual(area(10), 100)
       self.assertEqual(area(0), 0)
       self.assertIsInstance(area(5), int)

   def test_perimeter(self):
       self.assertEqual(perimeter(5), 20)
       self.assertEqual(perimeter(10), 40)
       self.assertEqual(perimeter(0), 0)
       self.assertIsInstance(perimeter(5), int)

   def test_area_exception(self):
       with self.assertRaises(ValueError):
           area(-5)

   def test_perimeter_exception(self):
       with self.assertRaises(ValueError):
           perimeter(-5)
