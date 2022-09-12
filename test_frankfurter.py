import unittest
from frankfurter import Frankfurter

class TestUrl(unittest.TestCase):
    """
    Class used for testing the url attributes of the Frankfurter class from checks.py
    """
    def test_frankfurter_url(self):

        f1 = Frankfurter()

        base_url: str = 'https://api.frankfurter.app'
        currencies_url: str = 'https://api.frankfurter.app/currencies'
        historical_url: str = 'https://api.frankfurter.app/'

        self.assertEqual(f1.base_url, base_url)
        self.assertEqual(f1.currencies_url, currencies_url)
        self.assertEqual(f1.historical_url, historical_url)

class TestCurrenciesList(unittest.TestCase):
    """
    Class used for testing the currencies attribute of the Frankfurter class from checks.py
    """
    def test_get_currencies_list(self):

        f1 = Frankfurter()
        currencies_url: str = 'https://api.frankfurter.app/currencies'

        self.assertEqual(f1.get_currencies_list(), f1.get_currencies_list())


class TestCheckCurrency(unittest.TestCase):
    """
    Class used for testing the Frankfurter.check_currency() method from frankfurter.py
    """

    def test_check_currency(self):

        f1 = Frankfurter()
        goodCurr = "INR"

        badCurr = 'AAA'
        f1.get_currencies_list()

        

        self.assertEqual(f1.check_currency(goodCurr), True)
        self.assertEqual(f1.check_currency(badCurr), False)



class TestHistoricalRate(unittest.TestCase):
    """
    Class used for testing the Frankfurter.get_historical_rate() method from frankfurter.py
    """
    def test_get_historical_rate(self):
        json_response = {'amount': 1.0, 'base': 'INR', 'date': '2020-06-09', 'rates': {'USD': 0.01324}}
        endpoint_url = 'https://api.frankfurter.app/2020-06-09?from=INR&to=USD'

        test_origin = 'INR'
        test_dest = 'USD' 
        test_date = '2020-06-09'
        f1 = Frankfurter()

        self.assertEqual(f1.get_historical_rate(test_origin,test_dest,test_date), json_response)

if __name__ == '__main__':
    unittest.main()