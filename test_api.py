import unittest
from api import call_get

class TestAPI(unittest.TestCase):
    """
    Class used for testing the call_get() function in api.py
    """
    def test_call_get(self):
        test_url = 'https://api.frankfurter.app'
        bad_url = 'https://api.frankfurter.app/2020-03-23&from=AUD&to=AED'
        test_status_code = 200
        self.assertEqual(call_get(test_url).status_code, test_status_code)

        with self.assertRaises(SystemExit) as cm:

            self.assertEqual(call_get(bad_url), cm.exception)
    

if __name__ == '__main__':
    unittest.main()
