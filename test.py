import unittest
import math
import circle
import rectangle
import triangle
import square

class ProjectTest(unittest.TestCase):
    #circle
    def test_circle_area(self):
        result = circle.area(10)
        self.assertEqual(result, 314.1592653589793)
        
    def test_circle_perimeter(self):
        result = circle.perimeter(10)
        self.assertEqual(result, 62.83185307179586)
        
    def test_circle_perimeter_zero(self):
        result = circle.perimeter(0)
        self.assertEqual(result, 0)
        
    def test_circle_area_zero(self):
        result = circle.area(0)
        self.assertEqual(result, 0)
    #triangle
    def test_triangle_area_zero(self):
        result = triangle.area(0, 10)
        self.assertEqual(result, 0)
        
    def test_triangle_peimeter_zero(self):
        result = triangle.perimeter(0, 1, 2)
        self.assertEqual(result, 0)
        
    def test_triangle_peimeter(self):
        result = triangle.perimeter(1,2,3)
        self.assertEqual(result, 6)
    
    def test_triangle_area(self):
        result = triangle.area(10,10)
        self.assertEqual(result, 50)
    #rectangle
    def test_rectangle_area(self):
        result = rectangle.area(10,50)
        self.assertEqual(result, 500)
    
    def test_rectangle_perimeter(self):
        result = rectangle.perimeter(10,50)
        self.assertEqual(result, 120)
        
    def test_rectangle_area_zero(self):
        result = rectangle.area(0, 10)
        self.assertEqual(result, 0)
        
    def test_rectangle_perimeter_zero(self):
        result = rectangle.perimeter(0, 10)
        self.assertEqual(result, 0)
    #square
    def test_square_area(self):
        result = square.area(10)
        self.assertEqual(result, 100)
        
    def test_square_perimeter(self):
        result = square.perimeter(10)
        self.assertEqual(result, 40)
        
    def test_square_perimeter_zero(self):
        result = square.perimeter(0)
        self.assertEqual(result, 0)
        
    def test_square_area_zero(self):
        result = square.area(0)
        self.assertEqual(result, 0)
        
if __name__ == '__main__':
    unittest.main()