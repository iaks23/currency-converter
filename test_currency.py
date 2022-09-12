import unittest
from currency import CurrencyConverter

class TestCurrencyConverterInstantiation(unittest.TestCase):
    """
    Class used for testing the instanciation of the CurrencyConverter class from currency.py
    """
   

    def test_currency_instance(self):
        test_amount = 1
        test_rate = 0
        test_from = 'USD'
        test_to = 'INR'
        test_date = '2020-03-23'
        c1 = CurrencyConverter(test_from,test_to,test_date)
        
         
        

        
        self.assertEqual(c1.amount,test_amount)
        self.assertEqual(c1.from_currency,test_from)

    

class TestCurrencyCheck(unittest.TestCase): 
    """
    Class used for testing the CurrencyConverter.check_currencies() method from currency.py
    """
    def test_currency_check(self):
        badCurr = 'AAA'
        test_from = 'USD'
        test_to = 'INR'
        test_date = '2020-03-23'
        c1 = CurrencyConverter(test_from,test_to,test_date)
        c2 = CurrencyConverter(badCurr,test_to,test_date) #Bad Origin Currency
        c3 = CurrencyConverter(test_from,badCurr,test_date) #Bad Destination Currency
        c4 = CurrencyConverter(badCurr,badCurr,test_date) #Both bad currency codes

        self.assertEqual(c1.check_currencies(),True)

        with self.assertRaises(SystemExit) as cm:
            self.assertEqual(c2.check_currencies(), cm.exception)
            
            
        with self.assertRaises(SystemExit) as cm:
            self.assertEqual(c3.check_currencies(), cm.exception)
        
        with self.assertRaises(SystemExit) as cm:
            self.assertEqual(c4.check_currencies(), cm.exception)



    

class TestReverseRate(unittest.TestCase):
    """
    Class used for testing the CurrencyConverter.reverse_rate() method from currency.py
    """

    def test_reverse_rate(self):
        test_from = 'USD'
        test_to = 'INR'
        test_date = '2020-03-23'
        c1 = CurrencyConverter(test_from,test_to,test_date)
        c1.rate = 76.166
        test_inverse = 0.0131

        self.assertEqual(c1.reverse_rate(), test_inverse)


    



    
    
class TestRoundRate(unittest.TestCase): 
    """
    Class used for testing the CurrencyConverter.round_rate() method from currency.py
    """
    def check_round_rate(self):
        test_from = 'USD'
        test_to = 'INR'
        test_date = '2020-03-23'
        testVal = 43.53568
        c1 = CurrencyConverter(test_from,test_to,test_date)
        self.assertEqual(c1.round_rate, 43.5357)

        testVal2 = 12.12345
        self.assertEqual(c1.round_rate, 12.1235)



class TestHistoricalRate(unittest.TestCase):
    """
    Class used for testing the CurrencyConverter.get_historical_rate() method from currency.py
    """
    def test_historical_rate(self):
        test_from = 'USD'
        test_to = 'INR'
        test_date = '2020-03-23'
        test_rate = '76.166'
        test_inverse = '0.0131'

        c1 = CurrencyConverter(test_from,test_to,test_date)
        expectedResponse = 'The conversion rate on '+test_date+' from '+test_from+' to '+test_to+' was '+test_rate+'. '+'The inverse rate was '+test_inverse+'.'

        with self.assertRaises(SystemExit) as cm:

            self.assertEqual(c1.get_historical_rate(), cm.exception)



        


    
    
if __name__ == '__main__':
    unittest.main()