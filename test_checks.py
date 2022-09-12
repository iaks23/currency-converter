import unittest
from checks import check_arguments, check_date
import sys


class TestCheckArguments(unittest.TestCase):
    """
    Class used for testing the check_arguments() function from checks.py
    """
    def test_check_arguments(self):
        input_args1 = ['x','y','z']
        input_args2 = ['a','b','c','d']
        input_args3 = [3,2]
        

        self.assertEqual(check_arguments(input_args1), input_args1)

       

        with self.assertRaises(SystemExit) as cm:

            self.assertEqual(check_arguments(input_args2), cm.exception)



class TestCheckDate(unittest.TestCase):
    """
    Class used for testing the check_date() function from checks.py
    """
    def test_check_date(self):
        goodDate = '2020-03-05'
        badDate = '2023/31/43'
        badDate2 = '2020-12-32'
        badDate3 = 'xyz'

        self.assertEqual(check_date(goodDate), True)

        with self.assertRaises(SystemExit) as cm:

            self.assertEqual(check_arguments(badDate), cm.exception)

        with self.assertRaises(SystemExit) as cm:
            self.assertEqual(check_arguments(badDate2), cm.exception)
        
        with self.assertRaises(SystemExit) as cm:
            self.assertEqual(check_arguments(badDate3), cm.exception)






if __name__ == '__main__':
    unittest.main()