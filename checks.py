import datetime
import sys

def check_arguments(args):
    """
    Function that will check if there are enough input arguments provided (ie exactly 3) and will return the input arguments if it is the case.
    Otherwise the program will exit and display the relevant message provided in the assignment brief

    Parameters
    ----------
    
    args : str
        Input argument to be checked

    Pseudo-code
    ----------
    
    BEGIN FUNCTION:
        if length of argument is exactly equal to 3
            return argument as it is
        else
            return self deifned error message

    Returns
    -------
    
    Input arguement as it is
    Error message as defined in assignment brief
    """

    # => To be filled by student
    if len(args) == 3:
        return args
    else:
        
        raise SystemExit('[ERROR] You need to provide 3 arguments in the following order: <date> <currency1> <currency2>')
    

def check_date(date):
    """
    Function that will check if the provided date is valid and will return the value True if that is the case. 
    Otherwise the program will exit and display the relevant message provided in the assignment brief

    Parameters
    ----------
    
    date : str
        input argument extracted to be checked

    Pseudo-code
    ----------
    
    BEGIN FUNCTION:
        TRY:
            Splitting input date based on - 
            Extracting the year,month,date
            validating date with datetime function
        EXCEPT:
            Throw exception for any value or type error

    Returns
    -------
    True if date is valid
    Error message if not
    """

    try:
        dateList = date.split("-")
        year = int(dateList[0])
        month = int(dateList[1])
        day = int(dateList[2])
        newDate = datetime.date(year,month,day)
        return True
    except Exception:
        
        raise SystemExit("Provided date is invalid")




    
  
   
