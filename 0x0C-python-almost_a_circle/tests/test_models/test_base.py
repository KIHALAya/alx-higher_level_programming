import unittest
from models.base import Base


class TestBase(unittest.TestCase):
    """
    Test cases for the Base class.
    """

    def test_base_id(self):
        """
        Test the automatic incrementation of id in Base class.
        """
        base_instance1 = Base()
        base_instance2 = Base()
        self.assertEqual(base_instance1.id, 1)
        self.assertEqual(base_instance2.id, 2)

    def test_base_custom_id(self):
        """
        Test the creation of Base instance with a custom id.
        """
        base_instance = Base(10)
        self.assertEqual(base_instance.id, 10)

    def test_to_json_string_empty(self):
        """
        Test converting an empty list of dictionaries to JSON string.
        """
        self.assertEqual(Base.to_json_string([]), "[]")

    def test_to_json_string_non_empty(self):
        """
        Test converting a list of dictionaries to JSON string.
        """
        dictionaries = [{"id": 1, "name": "John"}, {"id": 2, "name": "Alice"}]
        json_string = Base.to_json_string(dictionaries)

        expected_result = (
                '[{"id": 1, "name": "John"}, '
                '{"id": 2, "name": "Alice"}]'
                )

        sorted_actual = sorted(json_string)
        sorted_expected = sorted(expected_result)

        self.assertEqual(sorted_actual, sorted_expected)


if __name__ == '__main__':
    unittest.main()
