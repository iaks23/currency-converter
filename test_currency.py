import unittest
from currency import CurrencyConverter

class TestCurrencyConverterInstantiation(unittest.TestCase):
    """
    Class used for testing the instanciation of the CurrencyConverter class from currency.py
    """
    # => To be filled by student

class TestCurrencyCheck(unittest.TestCase): 
    """
    Class used for testing the CurrencyConverter.check_currencies() method from currency.py
    """
    # => To be filled by student

class TestReverseRate(unittest.TestCase):
    """
    Class used for testing the CurrencyConverter.reverse_rate() method from currency.py
    """
    # => To be filled by student
    
class TestRoundRate(unittest.TestCase): 
    """
    Class used for testing the CurrencyConverter.round_rate() method from currency.py
    """
    # => To be filled by student

class TestHistoricalRate(unittest.TestCase):
    """
    Class used for testing the CurrencyConverter.get_historical_rate() method from currency.py
    """
    # => To be filled by student
    
if __name__ == '__main__':
    unittest.main()