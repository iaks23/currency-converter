import sys
from currency import CurrencyConverter
from checks import check_arguments, check_date

if __name__ == "__main__":
    print("Launching converter...")
    """
    Main logics of the program.

    Pseudo-code
    ----------
    Extract the input arguments
    Remove the first argument (name of Python script)
    Check there are 3 items in the remaining list of argument (using your defined check_arguments() function)
    Check the validity of the input date (using your defined check_date() function)
    Instantiate an object from your defined CurrencyConverter class with the verified 2 currency codes and date
    Check the validity of the 2 currency codes (using your defined check_currencies() method from CurrencyConverter class)
    Extract the historical rate and calculate its inverse rate (using your defined get_historical_rate() method from CurrencyConverter class)
    """
    
    
    input_arg = sys.argv[1:]
    
    arg_resp = check_arguments(input_arg)
    if(arg_resp != input_arg):
        print("[ERROR] You need to provide 3 arguments in the following order: <date> <currency1> <currency2>")
        exit(0)
    
    date_resp = check_date(input_arg[0])
    if not date_resp:
        print("Provided date is invalid")
        exit(0)

    from_currency = str(input_arg[1])
    to_currency = str(input_arg[2])
    date = str(input_arg[0])

    curr1 = CurrencyConverter(from_currency,to_currency, date)

    currencyr_resp = curr1.check_currencies()

    final_val = curr1.get_historical_rate()

    

    
    

    

    

    

 


