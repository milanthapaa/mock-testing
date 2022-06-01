import unittest
from unittest.mock import patch
import main


class TestAdd(unittest.TestCase):
    def test_add(self):
        return self.assertEqual(main.add(10, 5), 15)


class TestJoke(unittest.TestCase):

    @patch('main.get_joke')
    def test_len_joke(self, mock_get_joke):
        mock_get_joke.return_value = "one"
        self.assertEqual(main.len_joke(), 3)


if __name__ == "__main__":
    unittest.main()
