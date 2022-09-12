import requests
import sys



def call_get(url: str) -> requests.models.Response:
    """
    Function that will call the API endpoint (input parameter) and return its response as a requests.models.Response object
    In case of an error, the program will exit and display the relevant message provided in the assignment brief

    Parameters
    ----------
    # => To be filled by student
    url: str
        URL of the API endpoint to be called, (Frankfurter)

    Pseudo-code
    ----------
    # => To be filled by student
    Define endpoint
    Call Function: call_get(endpoint: str)
    BEGIN FUNCTION:
    
        if response code is 200
            return requests.models.Response object
        else
            return error message as mentioned in brief



    Returns
    -------
    requests.models.Response object 
    API error message: There is an error with Frankfurter API
    """
    response = requests.get(url)
    if response.status_code == 200:
        return response
    else:
        raise SystemExit("There is an error with Frankfurter API")  
