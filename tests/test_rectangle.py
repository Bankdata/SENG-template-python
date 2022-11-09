import unittest
from rectangle import Rectangle
class TestRectangle(unittest.TestCase):

    def test_area(self):
        self.assertEqual(Rectangle(4.0, 3.0).get_area(), 12.0, "Should be 12.0")


if __name__ == '__main__':
    unittest.main()