import unittest
import math
from circle import area as circle_area, perimeter as circle_perimeter
from square import area as square_area, perimeter as square_perimeter
from triangle import area as triangle_area, perimeter as triangle_perimeter
from rectangle import area as rectangle_area, perimeter as rectangle_perimeter

class CircleTestCase(unittest.TestCase):
    def test_area_zero_radius(self):
        res = circle_area(0)
        self.assertEqual(res, 0)

    def test_area_positive_radius(self):
        res = circle_area(3)
        self.assertAlmostEqual(res, math.pi * 3 * 3)

    def test_area_negative_radius(self):
        with self.assertRaises(ValueError):
            circle_area(-3)

    def test_perimeter_zero_radius(self):
        res = circle_perimeter(0)
        self.assertEqual(res, 0)

    def test_perimeter_positive_radius(self):
        res = circle_perimeter(3)
        self.assertAlmostEqual(res, 2 * math.pi * 3)

    def test_perimeter_negative_radius(self):
        with self.assertRaises(ValueError):
            circle_perimeter(-3)

class SquareTestCase(unittest.TestCase):
    def test_area_zero_side(self):
        res = square_area(0)
        self.assertEqual(res, 0)

    def test_area_positive_side(self):
        res = square_area(4)
        self.assertEqual(res, 16)

    def test_area_negative_side(self):
        with self.assertRaises(ValueError):
            square_area(-4)

    def test_perimeter_zero_side(self):
        res = square_perimeter(0)
        self.assertEqual(res, 0)

    def test_perimeter_positive_side(self):
        res = square_perimeter(4)
        self.assertEqual(res, 16)

    def test_perimeter_negative_side(self):
        with self.assertRaises(ValueError):
            square_perimeter(-4)

class TriangleTestCase(unittest.TestCase):
    def test_area_zero_base_or_height(self):
        res = triangle_area(0, 10)
        self.assertEqual(res, 0)
        res = triangle_area(5, 0)
        self.assertEqual(res, 0)

    def test_area_positive_base_and_height(self):
        res = triangle_area(4, 5)
        self.assertEqual(res, 10)

    def test_area_negative_base_or_height(self):
        with self.assertRaises(ValueError):
            triangle_area(-4, 5)
        with self.assertRaises(ValueError):
            triangle_area(4, -5)

    def test_perimeter_positive_sides(self):
        res = triangle_perimeter(3, 4, 5)
        self.assertEqual(res, 12)

    def test_perimeter_negative_side(self):
        with self.assertRaises(ValueError):
            triangle_perimeter(-3, 4, 5)
        with self.assertRaises(ValueError):
            triangle_perimeter(3, -4, 5)
        with self.assertRaises(ValueError):
            triangle_perimeter(3, 4, -5)

class RectangleTestCase(unittest.TestCase):
    def test_area_zero_side(self):
        res = rectangle_area(10, 0)
        self.assertEqual(res, 0)

    def test_area_positive_sides(self):
        res = rectangle_area(10, 10)
        self.assertEqual(res, 100)

    def test_area_negative_side(self):
        with self.assertRaises(ValueError):
            rectangle_area(-10, 5)

    def test_perimeter_zero_side(self):
        res = rectangle_perimeter(10, 0)
        self.assertEqual(res, 20)

    def test_perimeter_positive_sides(self):
        res = rectangle_perimeter(10, 5)
        self.assertEqual(res, 30)

    def test_perimeter_negative_side(self):
        with self.assertRaises(ValueError):
            rectangle_perimeter(-10, 5)

if __name__ == '__main__':
    unittest.main()
