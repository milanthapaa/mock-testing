import unittest
from unittest.mock import patch, MagicMock
import main


class TestAdd(unittest.TestCase):
    def test_add(self):
        return self.assertEqual(main.add(10, 5), 15)


class TestJoke(unittest.TestCase):

    @patch('main.get_joke')
    def test_len_joke(self, mock_get_joke):
        mock_get_joke.return_value = "one"
        self.assertEqual(main.len_joke(), 3)

    @patch('main.requests')
    def test_get_joke(self, mock_requests):
        mock_response = MagicMock()
        mock_response.status_code = 200
        mock_response.json.return_value = {'value':
                                               {'joke': 'hello world'}
                                           }

        mock_requests.get.return_value = mock_response

        self.assertEqual(main.get_joke(), 'hello world')

    @patch('main.requests')
    def test_get_fail_joke(self, mock_requests):
        mock_response = MagicMock()
        mock_response.status_code = 403
        mock_response.json.return_value = {'value':
                                               {'joke': 'hello world'}
                                           }

        mock_requests.get.return_value = mock_response

        self.assertEqual(main.get_joke(), 'No jokes')


if __name__ == "__main__":
    unittest.main()
