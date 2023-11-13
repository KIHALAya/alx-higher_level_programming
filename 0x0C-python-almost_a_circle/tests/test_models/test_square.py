import unittest
from models.square import Square


class TestSquare(unittest.TestCase):
    """
    Test cases for the Square class.
    """

    def test_square_creation(self):
        """
        Test the creation of a Square instance with specified attributes.
        """
        square_instance = Square(7, 2, 3, 1)
        self.assertEqual(square_instance.size, 7)
        self.assertEqual(square_instance.x, 2)
        self.assertEqual(square_instance.y, 3)
        self.assertEqual(square_instance.id, 1)

    def test_size_property(self):
        """
        Test the size property of a Square instance.
        """
        square_instance = Square(5)
        square_instance.size = 8
        self.assertEqual(square_instance.size, 8)

    def test_update_method(self):
        """
        Test the update method of a Square instance.
        """
        square_instance = Square(4, 1, 2, 3)
        square_instance.update(5, 6, 7, 8)
        self.assertEqual(square_instance.id, 5)
        self.assertEqual(square_instance.size, 6)
        self.assertEqual(square_instance.x, 7)
        self.assertEqual(square_instance.y, 8)


if __name__ == '__main__':
    unittest.main()
