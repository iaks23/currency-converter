import sys
from frankfurter import Frankfurter

class CurrencyConverter:
    """
    Class that represents a Currency conversion object. It will be used to store the input arguments (currency codes, date) and also other information required (amount, rate, inverse rate, instantiation of Frankfurter class).

    Attributes
    ----------
    from_currency : str
        Code for the origin currency
    to_currency : str
        Code for the destination currency
    amount : float
        The amount (in origin currency) to be converted
    rate : float
        The conversion rate to be applied on the origin amount (origin -> destination)
    inverse_rate : float
        The inverse of the previous rate  (destination -> origin)
    date : str
        Date when the conversion rate was recorded
    api : Frankfurter
        Instance of Frankfurter class
    """
    def __init__(self, from_currency, to_currency, date):

        # => To be filled by student
        self.from_currency: str = from_currency

        self.to_currency: str = to_currency

        self.amount: float = 1

        self.rate: float = 0

        self.inverse_rate: float = 0

        self.date: str = date

        self.api = Frankfurter()


    def check_currencies(self):
        """
        Method that will check if currency codes stored in the class attributes are valid.
        Otherwise the program will exit and display the relevant message provided in the assignment brief

        Parameters
        ----------
        from_currency : str 
            Origin currency code
        to_currency : str
            Destination currency code
        

        Pseudo-code
        ----------
        BEGIN FUNCTION:
            Call method to retrieve currency list using Frankfurter instance
            Declare from_validity : bool
                Stores the result by checking if Origin Currency Code is valid using check_currency method
            Declare to_validity : bool
                Stores the result by checking if Origin Currency Code is valid using check_currency method

           
            BEGIN IF LOOP:
                IF BOTH from_validity and to_validity are FALSE THEN display error message of invalidity

                ELSE IF from_validity is FALSE THEN display error message saying from currency code is invalid

                ELSE IF to_validity is FALSE THEN display error message saying to currency code is invalid

                ELSE return TRUE since both codes are valid. 


        Returns
        -------
        Returns TRUE if both currency codes are Valid
        Otherwise, returns error message as defined in brief.
        """

        
        
        self.api.get_currencies_list()
        from_validity = self.api.check_currency(self.from_currency)
        to_validity = self.api.check_currency(self.to_currency)

        if not(from_validity) and not(to_validity):
            print(self.from_currency,"and",self.to_currency,"are not valid currency codes")

        elif not from_validity:
            print(self.from_currency, "is not a valid currency code")   
        elif not to_validity:
            print(self.to_currency,"is not a valid currency code")   
        else:
            return True

            

    def reverse_rate(self):
        """
        Method that will calculate the inverse rate from the value stored in the class attribute, round it to 4 decimal places and save it back in the class attribute inverse_rate.

        Parameters
        ----------
        self.rate: float 
            Value of rate retrieved by the API 

        Pseudo-code
        ----------
        Calculate the inverse of given rate by: 1/RATE
        Round the result to 4 decimals using ROUND()

        Returns
        -------
        Returns the inversed rate
        """
        self.inverse_rate = round((1/self.rate), 4)

        return self.inverse_rate
        

    def round_rate(self, rate):
        """
        Method that will round an input argument to 4 decimals places.

        Parameters
        ----------
        
        self.rate: float 
            Value of rate retrieved by the API 

        Pseudo-code
        ----------
        Round the rate to the nearest 4 decimals

        Returns
        -------
        Returns the rounded value
        """
        self.rate = round(self.rate, 4)
        return self.rate

        

    def get_historical_rate(self):
        """
        Method that will call the Frankfurter API and get the historical conversion rate for the currencies (rounded to 4 decimals) and date stored in the class attributes.
        Then it will calculate the inverse rate and will exit by displaying the relevant message provided in the assignment brief

        Parameters
        ----------
        from_currency : str 
            Origin currency code
        to_currency : str
            Destination currency code
        from_date : str
            Historical date required for transaction
        amount : float
            Amount of money to be converted, by default set to 1

        Pseudo-code
        ----------
        BEGIN FUNCTION:
            Call function to retrieve historic rate using Frankfurter instace. This returns a JSON response.

            Create a list with only the VALUES from the JSON response dict.
            
            Store the first value of the list in the rate variable. This now contains the required conversion value.
            
            Call the round function by passing the rate. 

            Call the reverse_rate function to calculate inverse rate and set it to the declared variable.
            
            Print the desired output as provided in brief


        Returns
        -------
        
        """
        api_resp = self.api.get_historical_rate(self.from_currency, self.to_currency, self.date, self.amount)
        
        rate_list = list(api_resp['rates'].values())
        self.rate = rate_list[0]
        self.rate = self.round_rate(self.rate)

        self.inverse_rate = self.reverse_rate()

        print("The conversion rate on",self.date,"from",self.from_currency,"to",self.to_currency,"was",self.rate,".","The inverse rate was",self.inverse_rate,".")



        

        