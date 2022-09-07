from api import call_get

class Frankfurter:
    """
    Class that manages API calls to Frankfurter. It will be used to store the URLS to the relevant endpoints. It will also automatically call the Currencies endpoint and store the return list of available currency codes.

    Attributes
    ----------
    base_url : str
        Base url to Frankfurter API
    currencies_url : str
        Frankfurter endpoint for extracting currencies list
    historical_url : str
        Frankfurter endpoint for extracting historical currencies conversion rates
    currencies: list
        List of available currency codes
    """
    def __init__(self):
        self.base_url: str = 'https://api.frankfurter.app'
        self.currencies_url: str = 'https://api.frankfurter.app/currencies'
        self.historical_url: str = 'https://api.frankfurter.app/'
        self.currencies: list = []

    def get_currencies_list(self):
        """
        Method that will get the list of available currencies and returns it as a Python list.

        Parameters
        ----------
        instance object that calls the currencies_url defined

        Pseudo-code
        ----------
        BEGIN FUNCTION:
            call call_get function from api.py using currencies_url
            store the returning dictionary in an object
            extract only the keys from dict and store in list
            

        Returns
        -------
        List of valid currency codes
        """
        data = call_get(self.currencies_url)
        self.currencies = list(data.keys())
        return self.currencies
        
        # => To be filled by student

    def check_currency(self, currency):
        """
        Method that will check if a provided currency code is valid and return True if that is the case.
        Otherwise it will return False.

        Parameters
        ----------
        # => To be filled by student
        Currency : str 
            The currency code that is to be validated

        Pseudo-code
        ----------
        # => To be filled by student
        BEGIN FUNCTION:
            Check if currency is available in list of currencies retrieved earlier

        Returns
        -------
        Return True if valid
        Else return False
        """
        if currency in self.currencies:
            return True
        else:
            return False
        
        # => To be filled by student

    def get_historical_rate(self, from_currency, to_currency, from_date, amount=1):
        """
        Method that will call the historical API endpoint in order to get the conversion rate for a given dates and currencies. It will return an requests.models.Response object.

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
        Declare endpoint URL so that it combines: 
            Historical URL + Date + Origin Currency Code + Destination Currency Code
        Call the api by passing the endpoint URL
        return the data reponse

        Returns
        -------
        requests.models.Response object in JSON format
        """
        
        endpoint = self.historical_url + from_date + "?from=" + from_currency +  "&to=" + to_currency
        data = call_get(endpoint)
        return data
