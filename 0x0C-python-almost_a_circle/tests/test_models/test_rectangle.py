import unittest
from models.rectangle import Rectangle
from unittest.mock import patch
from io import StringIO


class TestRectangle(unittest.TestCase):
    """
    Test cases for the Rectangle class.
    """

    def test_rectangle_creation(self):
        """
        Test the creation of a Rectangle instance
        with specified attributes.
        """
        rectangle_instance = Rectangle(10, 5, 2, 3, 1)
        self.assertEqual(rectangle_instance.width, 10)
        self.assertEqual(rectangle_instance.height, 5)
        self.assertEqual(rectangle_instance.x, 2)
        self.assertEqual(rectangle_instance.y, 3)
        self.assertEqual(rectangle_instance.id, 1)

    def test_area_calculation(self):
        """
        Test the calculation of the area of a Rectangle instance.
        """
        rectangle_instance = Rectangle(5, 4)
        self.assertEqual(rectangle_instance.area(), 20)


if __name__ == '__main__':
    unittest.main()
