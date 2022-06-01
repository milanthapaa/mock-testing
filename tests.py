import unittest
from main import add


class TestAdd(unittest.TestCase):
    def test_add(self):
        return self.assertEqual(add(10, 5), 15)


if __name__ == "__main__":
    unittest.main()
